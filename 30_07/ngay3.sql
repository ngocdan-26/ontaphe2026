CREATE DATABASE n30_07;
USE n30_07;

create table students(
	id int auto_increment primary key,
    name varchar(50) not null,
    email varchar(50) not null,
    age int not null
)