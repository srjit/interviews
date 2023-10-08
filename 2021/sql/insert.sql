 load data local infile '~/Downloads/myFile0.csv' into table money
 Fields terminated by ','
 enclosed by '"'
 lines terminated by '\n'
 (Id,firstname,lastname,country,balance,city)

create table money (Id VARCHAR(100),
       firstname VARCHAR(100),
       lastname VARCHAR(100),
       country VARCHAR(100),
       balance VARCHAR(100),
       city VARCHAR(100))

