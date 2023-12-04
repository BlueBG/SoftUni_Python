WITH ProductFeedbackStats AS (
    SELECT
        p.id AS product_id,
        p.name AS product_name,
        AVG(p.price) AS average_price,
        COUNT(f.id) AS total_feedbacks
    FROM
        products p
    INNER JOIN
        feedbacks f ON p.id = f.product_id
    WHERE
        p.price > 15
    GROUP BY
        p.id, p.name
    HAVING
        COUNT(f.id) > 1
)
SELECT
    product_name,
    ROUND(average_price, 2) AS average_price,
    total_feedbacks
FROM
    ProductFeedbackStats
ORDER BY
    total_feedbacks ASC,
    average_price DESC;
