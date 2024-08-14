
-- DROP TABLE IF EXISTS Staging_Games;

-- Create the Teams table
CREATE TABLE Teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

-- Create the Games table
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,
    team_id INT REFERENCES Teams(team_id),
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10)
);

-- Create the Offensive_Stats table
CREATE TABLE Offensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    passing_cmp INT,
    passing_att INT,
    completion_pct DECIMAL,  -- Assuming it's a percentage
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_avg DECIMAL,  -- Assuming it's a decimal
    rushing_td INT,
    total_plays INT,
    total_yards INT,
    avg_yds DECIMAL,  -- Assuming it's a decimal
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



-- Create the Defensive_Stats table
CREATE TABLE Defensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    opponent_passing_cmp INT,
    opponent_passing_att INT,
    opponent_completion_pct DECIMAL,  -- Assuming it's a percentage
    opponent_passing_yds INT,
    opponent_passing_td INT,
    opponent_rushing_att INT,
    opponent_rushing_yds INT,
    opponent_rushing_avg DECIMAL,  -- Assuming it's a decimal
    opponent_rushing_td INT,
    opponent_total_plays INT,
    opponent_total_yards INT,
    opponent_avg_yds DECIMAL,  -- Assuming it's a decimal
    opponent_pass_first_downs INT,
    opponent_rush_first_downs INT,
    opponent_first_down_pens INT,
    opponent_total_first_downs INT,
    opponent_total_penalties INT,
    opponent_total_penalties_yds INT,
    opponent_total_fum INT,
    opponent_total_int INT,
    opponent_total_to INT
);


-- Create the Special_Teams table
-- CREATE TABLE Special_Teams (
--     game_id INT REFERENCES Games(game_id),
--     fg_made INT,
--     fg_attempted INT,
--     fg_1_19 INT,
--     fg_20_29 INT,
--     fg_30_39 INT,
--     fg_40_49 INT,
--     fg_50_plus INT,
--     punt_yards INT,
--     avg_punt DECIMAL,
--     longest_fg INT,
--     xp_made INT,
--     points_scored INT
-- );


CREATE TABLE Kicking_Stats (
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

DROP TABLE IF EXISTS Punting_Stats;

CREATE TABLE Punting_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    punts INT,
    yds INT,
    avg DECIMAL(5, 2)  -- Assuming it's a decimal, up to two decimal places
);






-- Insert Teams into Database
INSERT INTO Teams (team_name) VALUES
('Oregon'),
('UCLA'),
('USC'),
('Washington');

-- Create the Staging_Games table with the correct column types
CREATE TABLE Staging_Games (
    date DATE,
    opponent VARCHAR(100),
    raw_location VARCHAR(10),
    result VARCHAR(10)
);


