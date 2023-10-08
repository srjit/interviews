
/*
events table

column	type
user_id	int
created_at	datetime
action	string
platform	string

The events table tracks every time a user performs a certain action (like, post_enter, etc.) on a platform (android, web, etc.).

Write a query to determine the top 5 actions performed during the month of November 2020, for actions performed on an Apple platform (iphone, ipad).

The output should include the action performed and their rank in ascending order. If two actions performed equally, they should have the same rank. 

*/


-- top 5 item_types for Sub-Saharan Africa region


SELECT ACTION,
       COUNT(*) as CNT,
       RANK() OVER (ORDER BY CNT DESC)
       WHERE CREATED AT BETWEEN '2020-11-01' and '2020-12-01'
FROM EVENTS GROUP BY
     ACTION 


select REGION, count(*) from sales where  Order_Date between '2014-01-01' and '2016-01-01' group by region

SELECT A.REGION, A.CNT,
RANK() OVER (ORDER BY A.CNT DESC) FROM
(SELECT REGION,
       COUNT(*) as CNT
       FROM SALES
       WHERE  ORDER_DATE BETWEEN '2014-01-01' AND '2016-01-01' 
       GROUP BY REGION) A;




select C.id, C.age, C.coins_needed, C.power from
(select A.id, A.code, A.coins_needed, A.power, B.age, B.is_evil from 
    wands A left outer join wands_property B
    on A.code = B.code) C where C.is_evil = 0 order by C.power, C.age desc;







select C.hacker_id, C.name, count(C.challenge_id) as challenges from
(select A.hacker_id, A.name, B.challenge_id from 
hackers A inner join challenges B on
A.hacker_id = B.hacker_id) C
group by C.hacker_id, C.name
order by challenges desc C.name desc
