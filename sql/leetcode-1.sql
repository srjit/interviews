

/*
 *
 * 184. Department Highest Salary: https://leetcode.com/problems/department-highest-salary/
 *
 */

SELECT TMP2.NAME, TMP2.DEPARTMENT, TMP2.SALARY FROM
(SELECT TMP1.NAME, TMP1.DEPARTMENT, TMP1.SALARY, RANK() OVER(PARTITION BY DEPARTMENTID ORDER BY SALARY DESC)  AS RANK_
FROM
(select A.NAME, A.SALARY, A.DEPARTMENTID, B.NAME AS
        DEPARTMENT FROM SALARIES A LEFT OUTER JOIN
        DEPARTMENT B on A.DEPARTMENTID = B.ID) TMP1) TMP2 WHERE RANK_ = 1


-- BETTER SOLUTION --

SELECT  B.NAME as DEPARTMENT, A.NAME as EMPLOYEE, A.SALARY
FROM 
(SELECT NAME,
       SALARY,
       DEPARTMENTID,
       RANK() OVER (PARTITION BY DEPARTMENTID ORDER BY SALARY DESC) AS RANK_
FROM SALARIES) A LEFT OUTER JOIN DEPARTMENT B ON A.DEPARTMENTID = B.ID WHERE A.RANK_ = 1
