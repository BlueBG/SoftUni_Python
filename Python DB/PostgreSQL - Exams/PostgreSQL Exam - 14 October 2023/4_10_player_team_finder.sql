CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
$$
    DECLARE
        player_full_name VARCHAR(50);
        current_team VARCHAR(45);

        BEGIN

            SELECT
                first_name || ' ' || last_name
            FROM
                players
            INTO
                player_full_name;


            SELECT
                t.name
            FROM
                teams AS t
            JOIN
                players AS p
            ON
                t.id = p.team_id
            WHERE
                p.first_name || ' ' || p.last_name = player_name
            INTO
                current_team;

            IF current_team IS NULL THEN
                team_name := 'The player currently has no team';
            ELSE
                team_name := current_team;
            END IF;

        END;
$$
LANGUAGE plpgsql;

