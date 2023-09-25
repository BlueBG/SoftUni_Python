SELECT
    id,
    CONCAT(
        "number",
        ' ',
        "street"
    ) AS "Addresses",
    city_id
FROM
    addresses
WHERE
    id >= 20