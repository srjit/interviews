
Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.



select NAME from
(select G.*, (G.SALARY - G.FR_SAL) as DIFF from  
(select E.NAME, E.SALARY, F.SALARY as FR_SAL from 
(select C.ID as ID, C.NAME as NAME, C.FRIEND_ID as FRIEND_ID, D.SALARY from
         (select A.ID as ID, A.NAME as NAME, B.FRIEND_ID as FRIEND_ID from
                 STUDENTS A left outer join
                 FRIENDS B on
                  A.ID = B.ID) C left outer join
            PACKAGES D on C.ID = D.ID) E join packages F on E.FRIEND_ID = F.ID) G) H
            WHERE DIFF < 0 
            ORDER BY ABS(FR_SAL);





-- Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
-- Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.


select distinct C.X1, C.Y1 from 
(select A.X as X1, A.Y as Y1, B.X as X2, B.Y as Y2 from
functions A join functions B on
A.X = B.Y and A.Y = B.X) C where C.X2 is not null and X1 <= Y1 order by X1

/*

TikTok Users: user_id | device_type | date
• A fact table with TikTok users' daily video views data: user_id | video_views | date

*/

select C.device_type, AVERAGE(C.views) from
(select A.user_id, A.device_type, B.vieo_views, B.date from
select * from users A inner join (select * from views where date between '2021-07-01' and '2021-08-01') B
on A.user_id = B.user_id) C group by C.device_type




--------------------------------------------------------------------------------------------------------------------------------------------------------------------



-- https://brainly.com/question/24548270 --




-- WEATHER STATION --


SET @N := 0;
SELECT COUNT(*) FROM STATION INTO @TOTAL;
SELECT
    ROUND(AVG(A.LAT_N), 4)
FROM (SELECT @N := @N +1 AS ROW_ID, LAT_N FROM STATION ORDER BY LAT_N) A
WHERE
    CASE WHEN MOD(@TOTAL, 2) = 0 
            THEN A.ROW_ID IN (@TOTAL/2, (@TOTAL/2+1))
            ELSE A.ROW_ID = (@TOTAL+1)/2
    END
;


SET @N := N + 1 -- := increment and set



select B.start_date, B.end_date 
FROM 
(select A.start_date, A.end_date, DATEDIFF(day, end_date, start_date) as TIME_TAKEN
FROM
    (select start_date from projects where start_date not in end_date,
    select end_date from projects where end_date not in start_date_date) A 
) B ORDER BY TIME_TAKEN





set @N=11;
create table contacts_duplicated as select * from contacts union (select @N := @N + 1 as id, first_name, last_name, email from contacts);


-- NON DUPLICATES --
select * from contacts where id in (select min_id from (select email, min(id) as min_id from contacts_duplicated group by email) A);


-- COALESCE --
-- Return the first non-null value in a list: --

SELECT COALESCE(NULL, NULL, NULL, 'W3Schools.com', NULL, 'Example.com');








select I.contest_id, I.hacker_id, I.name, sum(I.total_submissions) as total_sub, sum(I.total_accepted_submissions) as total_acc_sub, sum(I.total_views) as tot_views,
sum(total_unique_views) as total_uniq_views
from
(select G.contest_id, G.hacker_id, G.name, G.college_id, G.challenge_id, G.total_views, G.total_unique_views, H.total_submissions, H.total_accepted_submissions
from
(select E.contest_Id, E.hacker_id, E.name, E.college_id, E.challenge_id, F.total_views, F.total_unique_views
from 
(select C.contest_id, C.hacker_id, C.name, C.college_id, D.challenge_id
from
(select A.contest_id, A.hacker_id, A.name, B.college_id
       from contests A
            inner join
            colleges B
            on
            A.contest_id = B.contest_id) C

        inner join challenges D on
              C.college_id = D.college_id) E
        inner join view_stats F on
              E.challenge_id = F.challenge_id) G
        inner join submission_stats H on
              G.challenge_id = H.challenge_id) I
 where (I.total_sub + I.total_acc_sub + I.tot_views + I.total_unique_views) <> 0
 group by I.contest_id, I.hacker_id, I.name
 order by I.contest_id





select A.DOCTOR_NAMES 
from
(SELECT
      CASE WHEN OCCUPATION = 'Doctor' THEN NAME END AS DOCTOR_NAMES,
      CASE WHEN OCCUPATION = 'Professor' THEN NAME END AS PROFESSOR_NAMES,
      CASE WHEN OCCUPATION = 'Singer' THEN NAME END AS SINGER_NAMES,
      CASE WHEN OCCUPATION = 'Actor' THEN NAME END AS ACTOR_NAMES,
      CASE
        WHEN OCCUPATION = 'Doctor' THEN (@d := @d + 1)
        WHEN OCCUPATION = 'Professor' THEN (@p := @p + 1)
        WHEN OCCUPATION = 'Singer' THEN (@s := @s + 1)
        WHEN OCCUPATION = 'Actor' THEN (@a := @a + 1)
      END AS ROW_NUM
    FROM OCCUPATIONS
    ORDER BY NAME);
