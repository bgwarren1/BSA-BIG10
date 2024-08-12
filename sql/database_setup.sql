-- Drop the Staging_Games table if it exists to avoid any conflicts
DROP TABLE IF EXISTS Staging_Games;

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
    game_id INT REFERENCES Games(game_id),
    passing_cmp INT,
    passing_att INT,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_td INT,
    total_offense INT
);

-- Create the Defensive_Stats table
CREATE TABLE Defensive_Stats (
    game_id INT REFERENCES Games(game_id),
    passing_cmp INT,
    passing_att INT,
    passing_yds INT,
    passing_td INT,
    rushing_att INT,
    rushing_yds INT,
    rushing_td INT,
    total_offense INT,
    fumbles INT,
    interceptions INT,
    turnovers INT
);

-- Create the Special_Teams table
CREATE TABLE Special_Teams (
    game_id INT REFERENCES Games(game_id),
    fg_made INT,
    fg_attempted INT,
    fg_1_19 INT,
    fg_20_29 INT,
    fg_30_39 INT,
    fg_40_49 INT,
    fg_50_plus INT,
    punt_yards INT,
    avg_punt DECIMAL,
    longest_fg INT,
    xp_made INT,
    points_scored INT
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

-- If you wish to load data directly using SQL:
COPY Staging_Games (date, opponent, raw_location, result)
FROM '/Users/blairwarren/Desktop/BSA Article/bsa-big10-predictive-analysis/data/ucla_game_logs.csv'
DELIMITER ','
CSV HEADER;
