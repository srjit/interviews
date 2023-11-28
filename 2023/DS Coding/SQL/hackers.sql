
create table hackers(
    hacker_id INT,
    name VARCHAR(100)
);
INSERT into hackers(hacker_id, name) 
values 
    (5580, "Rose"),
    (8439, "Angela"),
    (27205, "Frank"),
    (52243, "Patrick"),
    (52348, "Lisa"),
    (57645, "Kimberly"),
    (77236, "Bonnie"),
    (83082, "Michael"),
    (86870, "Todd"),
    (90411, "Joe");


create table difficulty(difficulty_level INT, score INT);
INSERT into difficulty(difficulty_level, score) 
values 
    (1, 20),
    (2, 30),
    (3, 40),
    (4, 60),
    (5, 80),
    (6, 100),
    (7, 120);


create table challenges(challenge_id INT, hacker_id INT, difficulty_level INT);

insert into challenges(challenge_id, hacker_id, difficulty_level) 
values 
    (4810, 77726, 4),
    (21089, 27205, 1),
    (36566, 5580, 7),
    (66730, 52243, 6),  
    (71055, 52243, 2);


    