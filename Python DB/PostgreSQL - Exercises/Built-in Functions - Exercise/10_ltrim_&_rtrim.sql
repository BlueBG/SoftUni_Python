SELECT
    LTRIM(peak_name, 'M') AS "Left_Trim",
    RTRIM(peak_name, 'm') AS "Right_Trim"
FROM
    peaks;
