SELECT
    title,
    TRUNC(cost, 3) AS modifiled_price
FROM
    books

ORDER BY
    id
