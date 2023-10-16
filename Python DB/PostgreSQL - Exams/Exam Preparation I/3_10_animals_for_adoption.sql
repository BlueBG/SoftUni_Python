SELECT
    a.name,
    TO_CHAR(a.birthdate, 'YYYY') AS birthdate,
    at.animal_type
FROM
    owners AS o
RIGHT JOIN
    animals AS a
ON
    a.owner_id = o.id
JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
WHERE
    at.animal_type NOT IN ('Birds')
AND
    a.owner_id IS NULL
AND
    AGE('01/01/2022', a.birthdate) < '5 years'
ORDER BY
    a.name ASC;