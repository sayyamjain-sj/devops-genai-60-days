DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    experience INTEGER NOT NULL
);

INSERT INTO employees
VALUES
(1, 'Alice', 'Engineering', 95000, 3),
(2, 'Bob', 'HR', 65000, 5),
(3, 'Charlie', 'Engineering', 105000, 4),
(4, 'Diana', 'Data', 98000, 2),
(5, 'Ethan', 'DevOps', 110000, 4),
(6, 'Fatima', 'Data', 92000, 3),
(7, 'George', 'DevOps', 87000, 1);


.headers on
.mode column


-- Display all employees
SELECT * FROM employees;


-- 1. Find all DevOps employees
SELECT *
FROM employees
WHERE department = 'DevOps';


-- 2. Employees earning more than 95,000
SELECT name, salary
FROM employees
WHERE salary > 95000;


-- 3. Three highest-paid employees
SELECT name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;


-- 4. Unique departments
SELECT DISTINCT department
FROM employees;


-- 5. Engineering employees with more than 3 years experience
SELECT *
FROM employees
WHERE department = 'Engineering'
  AND experience > 3;


-- Bonus 1: Employees earning between 90,000 and 105,000
SELECT name, salary
FROM employees
WHERE salary BETWEEN 90000 AND 105000
ORDER BY salary DESC;


-- Bonus 2: Data or DevOps employees
SELECT name, department, salary
FROM employees
WHERE department IN ('Data', 'DevOps');


-- Bonus 3: Employees with 3 or fewer years experience
SELECT name, experience
FROM employees
WHERE experience <= 3
ORDER BY experience;