CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    creator_first_name VARCHAR(30)
) RETURNS INT
AS
$$
    DECLARE nuber_of_board_games INT;
    BEGIN

        SELECT
            COUNT(cbg.creator_id)
        INTO
            nuber_of_board_games
        FROM
            creators_board_games AS cbg
        LEFT JOIN
            creators AS c
        ON
            cbg.creator_id = c.id
        WHERE
            c.first_name = creator_first_name;
        RETURN nuber_of_board_games;
    END;
$$
LANGUAGE plpgsql;


