SELECT
    SUM(without_mountains) as countries_without_mountains
FROM
(SELECT
    COUNT(c.country_name) AS without_mountains
FROM
    countries AS c
LEFT JOIN
    mountains_countries AS mc
USING
    (country_code)
WHERE
    mc.country_code IS NULL
GROUP BY c.country_code) as subquery