

create table pages(
    page_id INT,
    page_name VARCHAR(100)
)


insert into pages (page_id, page_name) values 
(20001, 'SQL Solutions'),
(20045, 'Brain Exercises'),
(20701, 'Tips for Data Analysts');

create table page_likes(
    user_id int,
    page_id int,
    liked_date TIMESTAMP
)

insert into page_likes (user_id, page_id, liked_date) values  
(111, 20001, TIMESTAMP('2022-04-08 00:00:00')), 
(121, 20045, TIMESTAMP('2022-12-03 00:00:00')), 
(156, 20001, TIMESTAMP('2022-07-25 00:00:00'));

-- Write a query to return the IDs of the Facebook pages that have zero likes. 
-- The output should be sorted in ascending order based on the page IDs.



select C.page_id from 
    (select A.page_id, B.likes from pages A left join
        (select page_id, count(*) as likes from page_likes 
    GROUP BY page_id) B 
    ON A.page_id = B.page_id) 
    C
where C.likes IS NULL
order by page_id


SELECT pages.page_id
FROM pages
LEFT OUTER JOIN page_likes AS likes
  ON pages.page_id = likes.page_id
WHERE likes.page_id IS NULL;



SELECT page_id
FROM pages
WHERE page_id NOT IN (
    SELECT page_id
    FROM page_likes
)