
create table parts_assembly(
    part VARCHAR(20),
    finish_date TIMESTAMP,
    assembly_step INT
)

insert into parts_assembly (part, finish_date, assembly_step) values 
('battery', TIMESTAMP('2022-01-22 00:00:00'), 1),
('battery', TIMESTAMP('2022-02-22 00:00:00'),	2),
('battery', TIMESTAMP('2022-03-22 00:00:00'),	3),
('bumper', TIMESTAMP('2022-01-22 00:00:00'),	1),
('bumper',	TIMESTAMP('2022-02-22 00:00:00'), 2),
('bumper', NULL,	3),
('bumper',NULL,	4)


select part, assembly_step from parts_assembly
where finish_date is null
order by assembly_step 