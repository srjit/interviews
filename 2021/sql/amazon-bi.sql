

-- SALES Rank --
/*

Q: Think about Amazon selling millions of products by millions of sellers and the data model looks like below.

Table: Daily_Sales

Txn_date,   txn_id, marketplace, product,     seller_id, revenue,   Qty
04/26/2021   1234	 009         Liquid soap   98789	 200	    10

Q: Can you provide seller_ids whose monthly revenue for "April 2021" is in top 10?

*/



create table sales(
Region VARCHAR(50),
Country VARCHAR(50),
Item_Type VARCHAR(50),
Sales_Channel VARCHAR(50),
Order_Priority VARCHAR(50),
Order_Date DATE,
Order_ID INT,
Ship_Date DATE,
Units_Sold INT,
Unit_Price INT,
Unit_Cost INT,
Total_Revenue INT,
Total_Cost INT,
Total_Profit INT);




SELECT REGION, SUM(Total_Revenue) AS TOTAL_REV FROM SALES
 WHERE Order_Date BETWEEN '2014-01-01' and '2015-01-01'
GROUP BY REGION ORDER BY TOTAL_REV DESC LIMIT 3, 1


------------


-- Can you help how to identify top 2 sellers in each country and region for a given month? --

SELECT A.REGION, A.COUNTRY, SUM(A.TOTAL_REVENUE)
OVER (PARTITION BY A.REGION, A.COUNTRY)
FROM (select * from SALES where MONTH(ORDER_DATE) = 4) A;


SELECT A.REGION, A.MNTH, CEIL(AVG(TOTAL_REVENUE)) as REV
   FROM (SELECT *, MONTH(ORDER_DATE) AS MNTH
   FROM SALES HAVING MNTH IN (9,10,11)) A
   GROUP BY A.REGION, A.MNTH;

--------------------------------------------------



select * from (SELECT  REGION,
        RANK() OVER (PARTITION BY REGION ORDER BY TOTAL_REVENUE DESC) AS RANK_
FROM SALES) A having A.RANK_ in (1,2) ;


--------------------------------------------------
