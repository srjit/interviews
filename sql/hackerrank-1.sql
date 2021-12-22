
/*


HERMOINE WAND SELECTION

*/


SELECT C.ID, C.AGE, C.COINS_NEEDED, C.POWER 
FROM
(SELECT A.ID, A.COINS_NEEDED, A.POWER, B.AGE, B.IS_EVIL
FROM WANDS A INNER JOIN WANDS_PROPERTY B
ON A.CODE = B.CODE) C
WHERE C.IS_EVIL = 0
ORDER BY C.POWER DESC C.AGE DESC




create table Hackers (Hacker_Id Int, Name varchar(20));
insert into Hackers (Hacker_Id, Name) Values (4071, 'Rose'), (4806,'Angela'),(26071,'Frank'),(49438,'Patrick'),(74842,'Lisa'),(80305,'Kimberly'),(84072,'Bonnie'),(87868,'Michael'),(92118,'Todd'),(95895,'Joe')

create table Submissions (Submission_ID int, Hacker_Id int, Challenge_Id int, Score int)
insert into Submissions (Submission_ID, Hacker_Id, Challenge_Id, Score) Values (67194,74842,63132,76),(64479,74842,19797,98),(40742,26071,49593,20),(17513,4806,49593,32),(69846,80305,19797,19),(41002,26071,89343,36),(52826,49438,49593,9),
(31093,26071,19797,2),(81614,84072,49593,100),(44829,26071,89343,17),(75147,80305,49593,48),(14115,4806,49593,76),(6943,4071,19797,95),(12855,4806,25917,13),(73343,80305,49593,42),(84264,84072,63132,0),(9951,4071,49593,43),
(45104,49438,25917,34),(53795,74842,19797,5),(26363,26071,19797,29),(10063,4071,49593,96)





SELECT B.HACKER_ID, C.NAME, B.SCORE
FROM
(SELECT A.HACKER_ID, SUM(MAX_SCORE) as SCORE
FROM
(SELECT HACKER_ID, MAX(SCORE) AS MAX_SCORE
FROM SUBMISSIONS
GROUP BY HACKER_ID, CHALLENGE_ID) A GROUP BY A.HACKER_ID) B INNER JOIN
HACKERS C
ON B.HACKER_ID = C.HACKER_ID
ORDER BY B.SCORE DESC B.HACKER_ID DESC


SELECT B.HACKER_ID, HACKERS.NAME, B.SCORE FROM
(
SELECT A.HACKER_ID, SUM(MAX_SCORE) as SCORE
FROM
(SELECT HACKER_ID, MAX(SCORE) AS MAX_SCORE
FROM SUBMISSIONS
GROUP BY HACKER_ID, CHALLENGE_ID) A GROUP BY A.HACKER_ID HAVING SCORE > 0) B INNER JOIN HACKERS
ON B.HACKER_ID = HACKERS.HACKER_ID
ORDER BY B.SCORE, B.HACKER_ID



Select h.hacker_id, name, sum(score) as total_score
from
hackers as h inner join
/* find max_score*/
(select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score

on h.hacker_id=max_score.hacker_id
group by h.hacker_id, name

/* don't accept hackers with total_score=0 */
having total_score > 0

/* finally order as required */
order by total_score desc, h.hacker_id
;
