# Write your MySQL query statement below


select employee_id, 
        IF (employee_id%2!=0  AND name NOT LIKE 'M%', salary, 0) as bonus
FROM employees
ORDER BY employee_id;


