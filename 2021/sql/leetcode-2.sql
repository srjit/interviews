

/*

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


*/

SELECT
    IFNULL(
      (SELECT DISTINCT SALARY
       FROM SALARIES
       ORDER BY SALARY DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SECONDHIGHESTSALARY;
