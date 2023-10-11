SELECT
    MIN(avarage) AS min_average_area
FROM
    (SELECT
        AVG(area_in_sq_km) AS avarage
    FROM
        countries
    GROUP BY
        continent_code) AS subquery;
