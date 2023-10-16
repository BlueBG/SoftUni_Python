UPDATE coaches
SET salary = (SELECT
    c.salary * c.coach_level AS salary
FROM
    coaches AS c
LEFT JOIN
    players_coaches AS pc
ON
    c.id = pc.coach_id
LEFT JOIN
    players AS p
ON
    pc.player_id = p.id
WHERE
    c.first_name LIKE 'C%'
GROUP BY
c.first_name,
c.last_name,
c.salary,
c.coach_level
HAVING
    COUNT(pc.coach_id) > 1)


