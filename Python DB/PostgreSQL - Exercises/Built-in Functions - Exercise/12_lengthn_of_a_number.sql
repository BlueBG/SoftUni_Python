SELECT
    population,
    CHAR_LENGTH(CAST(population AS TEXT)) AS length
FROM
    countries