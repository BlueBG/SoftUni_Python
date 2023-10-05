CREATE TABLE mountains (
    id SERIAL PRIMARY KEY,
    name varchar(50)
);

CREATE TABLE peaks (
    id INT PRIMARY KEY,
    name varchar(50),
    mountain_id INT,
    CONSTRAINT fk_mountain_id
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
                ON DELETE CASCADE
);