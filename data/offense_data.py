import pandas as pd
import psycopg2

# Updated column names matching your CSV headers
column_names = [
    'Rk', 'Date', 'raw_location', 'Opponent', 'Result',
    'pass_cmp', 'pass_att', 'completion_pct', 'pass_yds', 'pass_td',
    'rush_att', 'rush_yds', 'rush_avg', 'rush_tds',
    'total_plays', 'total_yards', 'avg_yds',
    'pass_first_downs', 'rush_first_downs', 'first_down_pens', 'total_first_downs',
    'total_penalties', 'total_penalties_yds',
    'total_fum', 'total_int', 'total_to'
]

# Load the CSV file with updated headers
csv_file_path = '/Users/blairwarren/Desktop/BSA Article/bsa-big10-predictive-analysis/data/uw_offense_stats.csv'
df = pd.read_csv(csv_file_path, names=column_names, header=0)

# Drop rows with any NaN values (like the header row if it gets included as data)
df.dropna(inplace=True)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=4228,  
    database="postgres",  
    user="postgres",  
    password="Blairp11"  
)
cursor = conn.cursor()

# Delete existing data in Offensive_Stats
# cursor.execute("DELETE FROM Offensive_Stats")

# Insert the new data
for index, row in df.iterrows():
    try:
        # Insert the data directly into Offensive_Stats
        sql_query = """
            INSERT INTO Offensive_Stats (
                date, opponent, location, result, passing_cmp, passing_att, completion_pct, passing_yds, passing_td,
                rushing_att, rushing_yds, rushing_avg, rushing_td, total_plays, total_yards, avg_yds,
                pass_first_downs, rush_first_downs, first_down_pens, total_first_downs, total_penalties, total_penalties_yds,
                total_fum, total_int, total_to
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql_query, (
            row['Date'], row['Opponent'], row['raw_location'], row['Result'],
            row['pass_cmp'], row['pass_att'], row['completion_pct'], row['pass_yds'], row['pass_td'],
            row['rush_att'], row['rush_yds'], row['rush_avg'], row['rush_tds'],
            row['total_plays'], row['total_yards'], row['avg_yds'],
            row['pass_first_downs'], row['rush_first_downs'], row['first_down_pens'], row['total_first_downs'],
            row['total_penalties'], row['total_penalties_yds'],
            row['total_fum'], row['total_int'], row['total_to']
        ))

    except Exception as e:
        print("Error with row:", row.to_dict())
        print("Exception:", e)

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Offensive data successfully inserted!")
