-- UCLA
CREATE TABLE UCLA_Defensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    opponent_passing_cmp INT,
    opponent_passing_att INT,
    opponent_completion_pct DECIMAL,
    opponent_passing_yds INT,
    opponent_passing_td INT,
    opponent_rushing_att INT,
    opponent_rushing_yds INT,
    opponent_rushing_avg DECIMAL,
    opponent_rushing_td INT,
    opponent_total_plays INT,
    opponent_total_yards INT,
    opponent_avg_yds DECIMAL,
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


-- USC
CREATE TABLE USC_Defensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    opponent_passing_cmp INT,
    opponent_passing_att INT,
    opponent_completion_pct DECIMAL,
    opponent_passing_yds INT,
    opponent_passing_td INT,
    opponent_rushing_att INT,
    opponent_rushing_yds INT,
    opponent_rushing_avg DECIMAL,
    opponent_rushing_td INT,
    opponent_total_plays INT,
    opponent_total_yards INT,
    opponent_avg_yds DECIMAL,
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


-- Oregon
CREATE TABLE Oregon_Defensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    opponent_passing_cmp INT,
    opponent_passing_att INT,
    opponent_completion_pct DECIMAL,
    opponent_passing_yds INT,
    opponent_passing_td INT,
    opponent_rushing_att INT,
    opponent_rushing_yds INT,
    opponent_rushing_avg DECIMAL,
    opponent_rushing_td INT,
    opponent_total_plays INT,
    opponent_total_yards INT,
    opponent_avg_yds DECIMAL,
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


-- Washington
CREATE TABLE Washington_Defensive_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    opponent VARCHAR(100),
    location VARCHAR(50),
    result VARCHAR(10),
    opponent_passing_cmp INT,
    opponent_passing_att INT,
    opponent_completion_pct DECIMAL,
    opponent_passing_yds INT,
    opponent_passing_td INT,
    opponent_rushing_att INT,
    opponent_rushing_yds INT,
    opponent_rushing_avg DECIMAL,
    opponent_rushing_td INT,
    opponent_total_plays INT,
    opponent_total_yards INT,
    opponent_avg_yds DECIMAL,
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


-- We can just insert using the Defensive_Stats table
INSERT INTO UCLA_Defensive_Stats
SELECT *
FROM Defensive_Stats
WHERE game_id BETWEEN 1 AND 131; -- The game_id range where the school is present