-- UCLA
CREATE TABLE UCLA_Kicking_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    fg_1_19 INT,
    fg_20_29 INT,
    fg_30_39 INT,
    fg_40_49 INT,
    fg_50_plus INT,
    longest_fg INT,
    fg_percentage DECIMAL,
    fg_made INT,
    xp_made INT,
    points_scored INT
);


-- USC
CREATE TABLE USC_Kicking_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    fg_1_19 INT,
    fg_20_29 INT,
    fg_30_39 INT,
    fg_40_49 INT,
    fg_50_plus INT,
    longest_fg INT,
    fg_percentage DECIMAL,
    fg_made INT,
    xp_made INT,
    points_scored INT
);


-- Oregon
CREATE TABLE Oregon_Kicking_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    fg_1_19 INT,
    fg_20_29 INT,
    fg_30_39 INT,
    fg_40_49 INT,
    fg_50_plus INT,
    longest_fg INT,
    fg_percentage DECIMAL,
    fg_made INT,
    xp_made INT,
    points_scored INT
);

-- Washington
CREATE TABLE Washington_Kicking_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    fg_1_19 INT,
    fg_20_29 INT,
    fg_30_39 INT,
    fg_40_49 INT,
    fg_50_plus INT,
    longest_fg INT,
    fg_percentage DECIMAL,
    fg_made INT,
    xp_made INT,
    points_scored INT
);


-- We can just insert using the Defensive_Stats table
INSERT INTO UCLA_Kicking_Stats
SELECT *
FROM Kicking_Stats
WHERE game_id BETWEEN 1 AND 131; -- The game_id range where the school is present