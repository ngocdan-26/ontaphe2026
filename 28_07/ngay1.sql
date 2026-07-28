CREATE DATABASE n28_07;
use n28_07;

create table students(
	id int auto_increment primary key,
    name varchar(50) not null,
    email varchar(50) not null,
    age int not null
)