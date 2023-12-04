SELECT
    cl.full_name,
    COUNT(c.car_id) AS count_of_cars,
    SUM(COALESCE (c.bill, 0)) AS total_sum
FROM
    clients AS cl
RIGHT JOIN
    courses AS c ON c.client_id = cl.id
WHERE
    cl.full_name LIKE '_a%'
GROUP BY
    cl.full_name
HAVING
COUNT(c."id") > 1
ORDER BY
    cl.full_name

