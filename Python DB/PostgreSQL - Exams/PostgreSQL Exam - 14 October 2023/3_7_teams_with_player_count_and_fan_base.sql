SELECT
    t.id AS team_id,
    t.name AS team_name,
    COUNT(p.team_id)AS player_count,
    t.fan_base
FROM
    players AS p
RIGHT JOIN
    teams AS t
ON
    p.team_id = t.id
WHERE
    t.fan_base > 30000
GROUP BY
    t.id
ORDER BY
    player_count DESC,
    fan_base DESC