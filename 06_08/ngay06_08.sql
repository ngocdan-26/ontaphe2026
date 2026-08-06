create database n06_08;
use n06_08;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

