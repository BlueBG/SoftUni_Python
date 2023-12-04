SELECT
    i.name AS ingredient_name,
    p.name AS product_name,
    d.name AS distributor_name

FROM
    ingredients AS i
JOIN
    distributors AS d
ON
    d.id = i.distributor_id
JOIN
    products_ingredients AS pi
ON
    pi.ingredient_id = i.id
JOIN
    products AS p
ON
    p.id = pi.product_id

WHERE
    i.name ILIKE 'mustard'
AND
    d.country_id = 16
ORDER BY
    p.name ASC;

