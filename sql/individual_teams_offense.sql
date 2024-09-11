-- UCLA Offensive Stats Table
CREATE TABLE UCLA_Offensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    passing_cmp INT,
    passing_att INT,
    completion_pct DECIMAL,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_avg DECIMAL,
    rushing_td INT,
    total_plays INT,
    total_yards INT,
    avg_yds DECIMAL,
    pass_first_downs INT,
    rush_first_downs INT,
    first_down_pens INT,
    total_first_downs INT,
    total_penalties INT,
    total_penalties_yds INT,
    total_fum INT,
    total_int INT,
    total_to INT
);


-- USC Offensive Stats Table
CREATE TABLE USC_Offensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    passing_cmp INT,
    passing_att INT,
    completion_pct DECIMAL,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_avg DECIMAL,
    rushing_td INT,
    total_plays INT,
    total_yards INT,
    avg_yds DECIMAL,
    pass_first_downs INT,
    rush_first_downs INT,
    first_down_pens INT,
    total_first_downs INT,
    total_penalties INT,
    total_penalties_yds INT,
    total_fum INT,
    total_int INT,
    total_to INT
);


-- Oregon Offensive Stats Table
CREATE TABLE Oregon_Offensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    passing_cmp INT,
    passing_att INT,
    completion_pct DECIMAL,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_avg DECIMAL,
    rushing_td INT,
    total_plays INT,
    total_yards INT,
    avg_yds DECIMAL,
    pass_first_downs INT,
    rush_first_downs INT,
    first_down_pens INT,
    total_first_downs INT,
    total_penalties INT,
    total_penalties_yds INT,
    total_fum INT,
    total_int INT,
    total_to INT
);


-- Washington Offensive Stats Table
CREATE TABLE Washington_Offensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    passing_cmp INT,
    passing_att INT,
    completion_pct DECIMAL,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_avg DECIMAL,
    rushing_td INT,
    total_plays INT,
    total_yards INT,
    avg_yds DECIMAL,
    pass_first_downs INT,
    rush_first_downs INT,
    first_down_pens INT,
    total_first_downs INT,
    total_penalties INT,
    total_penalties_yds INT,
    total_fum INT,
    total_int INT,
    total_to INT
);


-- We can just insert using the Offensive_Stats table
INSERT INTO UCLA_Offensive_Stats
SELECT *
FROM Offensive_Stats
WHERE game_id BETWEEN 464 AND 596; -- The game_id range where the school is present



-- Add in drops
ALTER TABLE UCLA_Offensive_Stats
ADD COLUMN Drops INT;


-- Adding weather metric variables for UCLA
ALTER TABLE UCLA_Offensive_Stats
ADD COLUMN temp_f DECIMAL,
ADD COLUMN precipitation_in DECIMAL,
ADD COLUMN windspeed_mph DECIMAL,
ADD COLUMN altitude_m DECIMAL,
ADD COLUMN distance_from DECIMAL;


-- Adding weather metric variables to USC
ALTER TABLE UCLA_Offensive_Stats
ADD COLUMN temp_f DECIMAL,
ADD COLUMN precipitation_in DECIMAL,
ADD COLUMN windspeed_mph DECIMAL,
ADD COLUMN altitude_m DECIMAL,
ADD COLUMN distance_from DECIMAL;
