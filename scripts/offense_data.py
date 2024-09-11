import pandas as pd
import psycopg2

# Load CSV data
df = pd.read_csv('')


conn = psycopg2.connect(
    host="",
    port="",  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# Insert data back into the table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO UCLA_Offensive_Stats (date, raw_location, opponent, result, 
                                          passing_cmp, passing_att, completion_pct, passing_yds, 
                                          passing_td, rushing_att, rushing_yds, rushing_avg, 
                                          rushing_td, total_plays, total_yards, avg_yds, 
                                          pass_first_downs, rush_first_downs, first_down_pens, 
                                          total_first_downs, total_penalties, total_penalties_yds, 
                                          total_fum, total_int, total_to)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['Date'], row['raw_location'], row['Opponent'], row['Result'],
        row['pass_cmp'], row['pass_att'], row['completion_pct'], row['pass_yds'],
        row['pass_td'], row['rush_att'], row['rush_yds'], row['rush_avg'],
        row['rush_tds'], row['total_plays'], row['total_yards'], row['avg_yds'],
        row['pass_first_downs'], row['rush_first_downs'], row['first_down_pens'],
        row['total_first_downs'], row['total_penalties'], row['total_penalties_yds'],
        row['total_fum'], row['total_int'], row['total_to']
    ))

conn.commit()
cursor.close()
conn.close()
