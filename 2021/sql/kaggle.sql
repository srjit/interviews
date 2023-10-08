
/*

https://www.kaggle.com/getting-started/178151
*/


-- Write a query to list the top 3 cities which had the highest number of completed orders.


SELECT
    C.CITY, COUNT(C.ORDER_ID)
FROM
    (SELECT A.ORDER_ID, A.USER_ID, B.CITY
                FROM TRADES A
                INNER JOIN USERS
                ON A.USER_ID = B.USER_ID) C
GROUP BY C.CITY
