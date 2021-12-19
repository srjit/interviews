
/*

Think about Amazon selling millions of products by millions of sellers and the data model looks like below.

Table: Daily_Sales

Txn_date,   txn_id, marketplace, product,     seller_id, revenue,   Qty
04/26/2021   1234	 009         Liquid soap   98789	 200	    10

Q: Can you provide seller_ids whose monthly revenue for "April 2021" is in top 10?

*/


SELECT SELLER_ID, SUM(REVENUE) AS APRIL_REV FROM
DAILY_SALES WHERE TXN_DATE BETWEEN 04/01/2021 AND 05/01/2021
GROUP BY SELLER_ID
ORDER BY APRIL_REV DESC
LIMIT 10



/*

Q: Can you help how to identify top 2 sellers in each product and marketplace for a given month?

Expected Result:
Month Marketplace Product Seller_ID Seller_Revenue
April   009     Liquid Soap 98789   $10000000
April   009     Liquid Soap 12349   $9000000

April   009     Jenga Game  44488   $200000
April   009     Jenga Game  99909   $100000

April   007     Liquid Soap 34567   $10000000
April   007     Liquid Soap 23456   $9000000
*/

SELECT MONTH, MARKETPLACE, PRODUCT, SELLER_ID,  FROM
SELECT *, RANK() OVER(PARTITION BY Marketplace, Product, ORDER BY Seller_Revenue DESC) AS RANK_ A
WHERE RANK_ <= 2



/*

Q: Provide KPIs and report to answer the below situation

You need to create a operational review report for a call center business which receives calls 24X7. 

Goal: to optimize employee distribution among multiple (3) shifts in  a day. 

	Number. 1 of calls incoming at hour for a given day?
	2. Identify the overall call summary by status of the calls? 
    3. At any given minute of a day, we need to identify how many call were in progress?




KPI: % of the number of calls answered
     % of number of calls answered and issue has been resolved


Are all the employees trained for every type of problem?

Is the call centre localized to receive calls from a region?

- If it is for one region or a couple of timezons which are close -

We note an hourly volume of calls for a week or a month.
Depending on this there would be a consecutive set of 8 - hours  where we receive 


- If it is throughout the world - 


[Which of these three shifts recive the highest, second highest and least number of calls]

