-- =========================================================
-- Day 06 SQL Practice
-- Topics:
-- COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, WHERE
-- =========================================================


-- ---------------------------------------------------------
-- 1. Reset the table so this script can be rerun safely
-- ---------------------------------------------------------

DROP TABLE IF EXISTS employees;


-- ---------------------------------------------------------
-- 2. Create employees table
-- ---------------------------------------------------------

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    experience INTEGER NOT NULL
);


-- ---------------------------------------------------------
-- 3. Insert sample data
-- ---------------------------------------------------------

INSERT INTO employees (
    id,
    name,
    department,
    salary,
    experience
)
VALUES
    (1, 'Alice', 'Engineering', 95000, 3),
    (2, 'Bob', 'HR', 65000, 5),
    (3, 'Charlie', 'Engineering', 105000, 4),
    (4, 'Diana', 'Data', 98000, 2),
    (5, 'Ethan', 'DevOps', 110000, 4),
    (6, 'Fatima', 'Data', 92000, 3),
    (7, 'George', 'DevOps', 87000, 1);


-- ---------------------------------------------------------
-- SQLite output formatting
-- ---------------------------------------------------------

.headers on
.mode column


-- =========================================================
-- SECTION 1: Verify Data
-- =========================================================

SELECT *
FROM employees;


-- =========================================================
-- SECTION 2: COUNT
-- =========================================================

-- Count total number of employees

SELECT
    COUNT(*) AS total_employees
FROM employees;


-- Count employees with a non-null salary

SELECT
    COUNT(salary) AS employees_with_salary
FROM employees;


-- =========================================================
-- SECTION 3: SUM
-- =========================================================

-- Calculate total salary expense

SELECT
    SUM(salary) AS total_salary
FROM employees;


-- =========================================================
-- SECTION 4: AVG
-- =========================================================

-- Calculate average salary

SELECT
    ROUND(AVG(salary), 2) AS average_salary
FROM employees;


-- =========================================================
-- SECTION 5: MIN and MAX
-- =========================================================

-- Find lowest and highest salaries

SELECT
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary
FROM employees;


-- Find minimum and maximum experience

SELECT
    MIN(experience) AS minimum_experience,
    MAX(experience) AS maximum_experience
FROM employees;


-- =========================================================
-- SECTION 6: GROUP BY
-- =========================================================

-- Count employees in each department

SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;


-- Average salary by department

SELECT
    department,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;


-- Total salary by department

SELECT
    department,
    SUM(salary) AS total_department_salary
FROM employees
GROUP BY department
ORDER BY total_department_salary DESC;


-- Minimum and maximum salary by department

SELECT
    department,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees
GROUP BY department
ORDER BY department;


-- Average experience by department

SELECT
    department,
    ROUND(AVG(experience), 2) AS average_experience
FROM employees
GROUP BY department
ORDER BY average_experience DESC;


-- =========================================================
-- SECTION 7: WHERE + GROUP BY
-- =========================================================

-- Only employees with at least 2 years of experience,
-- grouped by department

SELECT
    department,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
WHERE experience >= 2
GROUP BY department
ORDER BY average_salary DESC;


-- Only employees earning at least 90,000,
-- grouped by department

SELECT
    department,
    COUNT(*) AS high_salary_employees
FROM employees
WHERE salary >= 90000
GROUP BY department
ORDER BY high_salary_employees DESC;


-- =========================================================
-- SECTION 8: HAVING
-- =========================================================

-- Departments with at least 2 employees

SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY employee_count DESC;


-- Departments with average salary greater than 90,000

SELECT
    department,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 90000
ORDER BY average_salary DESC;


-- Departments with total salary greater than 180,000

SELECT
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 180000
ORDER BY total_salary DESC;


-- =========================================================
-- SECTION 9: WHERE vs HAVING Example
-- =========================================================

-- WHERE filters rows before grouping.
-- HAVING filters grouped results after aggregation.

SELECT
    department,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
WHERE experience >= 2
GROUP BY department
HAVING AVG(salary) > 90000
ORDER BY average_salary DESC;


-- =========================================================
-- SECTION 10: Interview-Style Queries
-- =========================================================

-- 1. Which department has the highest average salary?

SELECT
    department,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC
LIMIT 1;


-- 2. Which department has the most employees?

SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC
LIMIT 1;


-- 3. Find departments where the maximum salary
-- is greater than 100,000

SELECT
    department,
    MAX(salary) AS highest_salary
FROM employees
GROUP BY department
HAVING MAX(salary) > 100000
ORDER BY highest_salary DESC;


-- 4. Find departments where average experience
-- is at least 3 years

SELECT
    department,
    ROUND(AVG(experience), 2) AS average_experience
FROM employees
GROUP BY department
HAVING AVG(experience) >= 3
ORDER BY average_experience DESC;


-- 5. Count employees by department whose salary
-- is above 90,000

SELECT
    department,
    COUNT(*) AS employees_above_90000
FROM employees
WHERE salary > 90000
GROUP BY department
ORDER BY employees_above_90000 DESC;


-- =========================================================
-- END OF DAY 06 SQL PRACTICE
-- =========================================================