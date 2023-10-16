CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department)
RETURNS INTEGER
AS
$$
    DECLARE
    searched_volunteers_department
    BEGIN
        SELECT
            COUNT(vd.id)
        FROM
            volunteers AS v
        LEFT JOIN
            volunteers_departments AS vd
        ON
            v.department_id = vd.id
        RETURN searched_volunteers_department
    END
$$
LENGUAGE plpgsql;



SELECT
    COUNT(vd.id)
FROM
    volunteers AS v
LEFT JOIN
    volunteers_departments AS vd
ON
    v.department_id = vd.id