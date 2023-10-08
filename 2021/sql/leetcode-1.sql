
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


/*
 *
 * 180. Consecutive Numbers : https://leetcode.com/problems/consecutive-numbers/
 *
 */

SELECT DISTINCT A.NUM AS "CONSECUTIVENUMS" FROM
(SELECT NUM,
       LEAD(NUM, 1) OVER (ORDER BY ID) AS LEAD1,
       LEAD(NUM, 2) OVER (ORDER BY ID) AS LEAD2 FROM LOGS) A
WHERE (A.NUM = A.LEAD1) AND (A.LEAD1 = A.LEAD2)
      

/*
 *
 * https://leetcode.com/problems/nth-highest-salary/
 *
 */
SELECT SALARY FROM SALARIES ORDER BY SALARY DESC LIMIT 2,1;


/*
 *
 * RANK Scores: https://leetcode.com/problems/rank-scores/
 * 
 */
SELECT SCORE, DENSE_RANK() OVER (ORDER BY SCORE DESC) `RANK` FROM SCORES;



/*
 *
 * 626. Exchange Seats:  https://leetcode.com/problems/exchange-seats/
 *
 */


SELECT C.ID, case
       when C.B_NAME is not NULL then C.B_NAME
       else C.A_NAME
       end as STUDENT
     from
(Select A.ID, A.EXCHANGE, A.STUDENT as A_NAME, B.STUDENT as B_NAME FROM 
(SELECT ID, STUDENT, CASE
           WHEN MOD(ID, 2) = 0 THEN ID-1
            ELSE ID+1
            END
        as EXCHANGE
        FROM SEAT) A LEFT OUTER JOIN SEAT B on A.EXCHANGE = B.ID) C ;
