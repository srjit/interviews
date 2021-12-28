

/*

 Provided a table with user_id and the dates they visited the platform, find the top 3 users with the longest continuous streak of visiting the platform as of yesterday

Lowest Averge = Most continuous streak


https://blog.jooq.org/how-to-find-the-longest-consecutive-series-of-events-in-sql/

*/

create table
       fblogin(date DATE,
               id VARCHAR(10));

  
load data local infile "fb-login-data.csv" into table fblogin fields terminated by "," lines terminated by "\n";


select B.ID, AVG(B.DIFF) AS AVG_DIFF
FROM
(select A.ID,
       DATEDIFF(A.DATE, A.LAG_DATE) as DIFF
FROM
(select ID,
       DATE,
       LAG(DATE)
 OVER (PARTITION BY ID ORDER BY DATE) as LAG_DATE
     FROM fblogin) A WHERE A.DATE >= "2021-09-20") B
     GROUP BY B.ID
ORDER BY AVG_DIFF
