SELECT
    c.id,
    CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
    c.email
FROM
    creators c
LEFT JOIN
    creators_board_games cbg
ON
    cbg.creator_id = c.id
WHERE
    cbg.creator_id IS NULL
ORDER BY
    creator_name ASC;


