SELECT
    CONCAT_WS(
        ' ',
        m.mountain_range,
        p.peak_name
    ) AS "Mountain Information",
    CHAR_LENGTH(CONCAT_WS(
        ' ',
        m.mountain_range,
        p.peak_name
    )) AS "Characters Length",
    BIT_LENGTH(CONCAT_WS(
        ' ',
        m.mountain_range,
        p.peak_name
    )) AS "Bits of a String"
FROM
    peaks AS p,
    mountains AS m
WHERE
    p.mountain_id = m.id

