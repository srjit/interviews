
Department and second highest salary from each department

SELECT A.Department, A.SALARY FROM (SELECT Department, SALARY, DENSE_RANK() OVER (PARTITION BY DEPARTMENT ORDER BY SALARY DESC) as SALARY_RANK
FROM EMPLOYEE) A WHERE A.SALARY_RANK = 2;

query to extract item names that were abover average order total


- Given a table of data, how would you create a model to detect spam?


- Provided a table with user_id and the dates they visited the platform, find the top 100 users with the longest continuous streak of visiting the platform as of yesterday.
