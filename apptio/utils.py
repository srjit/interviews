import os, gzip
from tqdm import tqdm
import json
from datetime import datetime
import gc

import sqlalchemy
from sqlalchemy import create_engine, types
from sqlalchemy.dialects.mysql import LONGTEXT

import pandas as pd
pd.set_option('display.max_columns', None)
                        
import warnings
warnings.filterwarnings('ignore')

def get_gzip_file_paths(root_dir):
    
    '''
        Gzipped files are where the clickthrough data is stored.
        Collect all the gzip paths recursively starting the traversal
        from the root_directory
        
        @return List of gzips (clickthrough files)
    '''
    
    gzip_file_paths = []
    for subdir, dirs, files in tqdm(os.walk(root_dir)):

        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".gz"):
                gzip_file_paths.append(filepath)
                
    return gzip_file_paths



def validate_and_get_schema(path):
    
    try:
        df = pd.read_json(path, lines=True, compression='gzip')
       
        df["request_keys"] = df["request"].apply(lambda x: x.keys())
        df["server_request_keys"] = df["server_request"].apply(lambda x: x.keys())

        # some lines might have some new keys, so reading the whole gzip is necessary
        request_attributes_all = [list(x) for x in df["request_keys"].tolist()]
        request_attributes = list(set([item for sublist in request_attributes_all for item in sublist]))
        
        serv_request_attributes_all = [list(x) for x in df["server_request_keys"].tolist()]
        serv_request_attributes = list(set([item for sublist in serv_request_attributes_all for item in sublist]))

        schema = request_attributes + serv_request_attributes + ["request_datetime"]
        
        columns_to_remove = ["country_code", "requestType", "is_online", "method", "accept_language", "user_map"]        
        [schema.remove(col) for col in columns_to_remove if col in schema]
        
        df = None
        gc.collect()
        
        return schema
    except:
        return None
    
    
def find_full_schema(gzip_paths):
    
    successful_paths = []
    failed_paths = []
    
    schema = []
    
    for path in tqdm(gzip_paths):
        schema_ = validate_and_get_schema(path)
        if schema_ is None:
            failed_paths.append(path)
        else:
            new_columns = [x for x in schema_ if x not in schema]
            schema = schema + new_columns
            successful_paths.append(path)
            
    return schema, successful_paths, failed_paths
            
    
    
def standardize_data(path, schema):
    
    try:
        df = pd.read_json(path, lines=True, compression='gzip')
        df["request_keys"] = df["request"].apply(lambda x: x.keys())
        df["server_request_keys"] = df["server_request"].apply(lambda x: x.keys())
        
        df["filepath"] = path.split("clickstream_data_2016")[1][1:]

        request_attributes_all = [list(x) for x in df["request_keys"].tolist()]
        request_attributes = list(set([item for sublist in request_attributes_all for item in sublist]))
        for attribute in request_attributes:
            df[attribute] = df["request"].apply(lambda x: x[attribute] if attribute in x else None)

        serv_request_attributes_all = [list(x) for x in df["server_request_keys"].tolist()]
        serv_request_attributes = list(set([item for sublist in serv_request_attributes_all for item in sublist]))
        for attribute in serv_request_attributes:
            df[attribute] = df["server_request"].apply(lambda x: x[attribute] if attribute in x else None)
            
        df["request_datetime"] = df["request_unixtime"].apply(lambda x: datetime.fromtimestamp(x))
    
        cols_to_remove = ["request_keys", "server_request_keys", "request", "server_request" ,"request_unixtime", "user_map"]
        for col in cols_to_remove:
            if col in df.columns:
                del df[col]
        
        missing_cols = [x for x in schema if x not in df.columns.tolist()]
        if len(missing_cols) > 0:
            for col in missing_cols:
                df[col] = None
        df = df[schema]
        
        return df
    
    except Exception as e:
        print(e)
        return None
    
    
def standardize_and_store(paths, schema, table, connection):
    
    status_dfs = []
    df = None
    tmps = []
    for path in tqdm(paths):
    
        df = standardize_data(path, schema)
        
        #Take care of any new status fields
        status_columns = ["statusCode", "statusLine", "error"]
        status_df = df[status_columns]
        status_df.drop_duplicates(inplace=True)
        status_dfs.append(status_df)
        
        del df["statusLine"]
        del df["error"]
        
        # x_forwarded_for - is the ip address of the person who clicked, not "ip"
        # verified using providing values in an ip lookup : https://www.iplocation.net/ip-lookup
        
        # Take care of User fields - Assumption: One user is using only one device at a time
        # Bug in code - the same user might come in multiple gzips - then there could be a duplication issue - FIX LATER
        user_columns = ["user_agent", "x_forwarded_for"]
        user_df = df[user_columns]
        user_df.drop_duplicates(inplace=True)
        
        user_type_map = {x:LONGTEXT for x in user_columns}
        user_type_map["user_map"] = types.JSON
        user_df.to_sql(name="users", con=connection, dtype=user_type_map, index=False, if_exists='append')

        # Rest of the columns are events - Take care of that
        columns_to_ignore_by_event_df = status_columns + user_columns + ["request_unixtime"]
        event_columns = [x for x in df.columns.tolist() if x not in columns_to_ignore_by_event_df ] + ["statusCode", "x_forwarded_for", "request_datetime"]
        event_df = df[event_columns]
        
        event_type_map = {x:LONGTEXT for x in event_columns}
        event_type_map["responseHeaders"] = types.JSON
        event_type_map["requestHeaders"] = types.JSON
        event_df.to_sql(name="events", con=connection, dtype=event_type_map, index=False, if_exists='append')
        
        event_df = None
        user_df = None
        
        del event_df
        del user_df
        
        gc.collect()
        
    status = pd.concat(status_dfs)
    status.drop_duplicates()
    status_type_map = {x:LONGTEXT for x in schema}
    status_type_map["user_map"] = types.JSON
    status.to_sql(name="status", con=connection, dtype=status_type_map, index=False, if_exists='append')
    
    
def read_gzip_files(gzip_file_paths, swap_path, failed_filename):
    
    '''
    Read the gzipped files into a dataframe and 
    construct the clickthrough attributes.
    
    @return List of dataframes with clickthrough attributes, 
            one for each file
    @return List of dataframes which have
    '''

    json_data = list(map(parse_clickthrough_gzip, gzip_file_paths))
    failed_files = [gzip_file_paths[i] for i, df in enumerate(json_data) if df is None]
    
    write_failed_filelist(failed_files, swap_path, failed_filename)
    
    return json_data