SELECT
    p.id,
    p.first_name || ' ' || p.last_name AS full_name,
    p.age,
    p.position,
    p.salary,
    sd.pace,
    sd.shooting
FROM
    players AS p
JOIN
    skills_data AS sd
ON
    p.skills_data_id = sd.id
WHERE
    p.position = 'A'
AND
    p.team_id IS NULL
GROUP BY
    p.id,
    sd.pace,
    sd.shooting
HAVING
    SUM(sd.pace + sd.shooting) > 130
