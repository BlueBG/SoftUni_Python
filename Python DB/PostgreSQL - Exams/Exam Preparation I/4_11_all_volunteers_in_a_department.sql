DROP FUNCTION IF EXISTS fn_get_volunteers_count_from_department(VARCHAR(30));

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
searched_volunteers_department VARCHAR(30)
)
RETURNS INTEGER
AS
$$

    BEGIN
        RETURN(
        SELECT
            COUNT(vd.id)
        FROM
            volunteers AS v
        LEFT JOIN
            volunteers_departments AS vd
        ON
            v.department_id = vd.id
        WHERE
            vd.department_name = searched_volunteers_department);

    END;
$$

LANGUAGE plpgsql;


