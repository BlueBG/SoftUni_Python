UPDATE countries
SET
    country_code = LOWER(reverse(country_code))