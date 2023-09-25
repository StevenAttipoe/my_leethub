SELECT max(salary) as SecondHighestSalary
from Employee
WHERE salary < (SELECT max(salary) from Employee);

# ORDER BY value, LIMIT n-1 OFFSET n
# SELECT IFNULL(
#   NULL, (
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY Salary DESC
#     LIMIT 1, 1
#   )
# ) AS SecondHighestSalary;