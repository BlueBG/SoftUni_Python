SELECT
    COUNT(employee_id) AS count
FROM
    employees AS e
WHERE
    e.salary > (
        SELECT
            AVG(salary) AS avg_salary
        FROM
            employees
        );