



https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

SELECT CASE
    WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
    END
FROM BST
ORDER BY N ASC

-- selecting from multiple tables

https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

SELECT c.company_code, c.founder, 
    COUNT(DISTINCT l.lead_manager_code), count(distinct s.senior_manager_code), 
    count(distinct m.manager_code),count(distinct e.employee_code) 
from Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e 
where c.company_code = l.company_code 
    and l.lead_manager_code=s.lead_manager_code 
    and s.senior_manager_code=m.senior_manager_code 
    and m.manager_code=e.manager_code 
group by c.company_code order by c.company_code;


--- Find a triangle from 3 columns or NOT ---

SELECT CASE             
            WHEN A + B > C AND B + C > A AND A + C > B THEN
                CASE 
                    WHEN A = B AND B = C THEN 'Equilateral'
                    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
                    ELSE 'Scalene'
                END
            ELSE 'Not A Triangle'
        END
FROM TRIANGLES;



--- Pivot --

https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true

SELECT
    [Doctor], [Professor], [Singer], [Actor]
FROM
(
    SELECT ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) [RowNumber], * FROM OCCUPATIONS
) AS tempTable
PIVOT
(
    MAX(NAME) FOR OCCUPATION IN ([Doctor], [Professor], [Singer], [Actor])
) AS pivotTable















------------ Find Median -----------

set @N=0;
select count(*) from STATION into @TOTAL;
SELECT
	ROUND(AVG(A.LAT_N), 4)
FROM
	(select @N := N+1 AS ROW_ID, LAT_N from STATION) A

WHERE
	CASE WHEN MOD(@TOTAL, 2) = 0 THEN A.ROW_ID IN (@TOTAL/2, @TOTAL/2 + 1)
	ELSE A.ROW_ID = (@TOTAL + 1)/2

	END
;


----------------------------------------------

select h.hacker_id, h.name
from submissions s
inner join challenges c
on s.challenge_id = c.challenge_id
inner join difficulty d
on c.difficulty_level = d.difficulty_level 
inner join hackers h
on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc

----------------------------------------------

SELECT IF(GRADE < 8, NULL, NAME), GRADE, MARKS
FROM STUDENTS JOIN GRADES
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC, NAME

----------------------------------------------
