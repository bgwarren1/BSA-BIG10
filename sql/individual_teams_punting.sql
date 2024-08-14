-- UCLA Punting Stats Table
CREATE TABLE UCLA_Punting_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    punts INT,
    yds INT,
    avg DECIMAL
);

-- USC Punting Stats Table
CREATE TABLE USC_Punting_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    punts INT,
    yds INT,
    avg DECIMAL
);

-- Washington Punting Stats Table
CREATE TABLE Washington_Punting_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    punts INT,
    yds INT,
    avg DECIMAL
);

-- Oregon Punting Stats Table
CREATE TABLE Oregon_Punting_Stats (
    game_id SERIAL PRIMARY KEY,
    date DATE,
    raw_location VARCHAR(50),
    opponent VARCHAR(100),
    result VARCHAR(10),
    punts INT,
    yds INT,
    avg DECIMAL
);
