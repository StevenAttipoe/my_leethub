SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address AS a
ON p.personId = a.personId;