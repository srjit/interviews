import os, gzip
from tqdm import tqdm
import json
from datetime import datetime
import gc


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

        schema = ["request", "server_request"] + request_attributes + serv_request_attributes
        
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

        del df["request_keys"]
        del df["server_request_keys"]
        del df["request"]
        del df["server_request"]
        
        missing_cols = [x for x in schema if x not in df.columns.tolist()]
        if len(missing_cols) > 0:
            for col in missing_cols:
                df[col] = None
        df = df[schema]
        
        return df
    
    except Exception as e:
        print(e)
        return None
    
    
def standardize_and_store(paths, schema, table, connection, type_map):
    
    for path in paths:
    
        df = standardize_data(path, schema)
        df.to_sql(name=table, con=connection, dtype=type_map, index=False, if_exists='append')
        
        df = None
        del df
        
        gc.collect()
    

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