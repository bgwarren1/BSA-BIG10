import pandas as pd
import psycopg2

# Updated column names matching your CSV headers
column_names = [
    'Rk', 'Date', 'raw_location', 'Opponent', 'Result',
    'opponent_pass_cmp', 'opponent_pass_att', 'opponent_completion_pct', 'opponent_pass_yds', 'opponent_pass_td',
    'opponent_rush_att', 'opponent_rush_yds', 'opponent_rush_avg', 'opponent_rush_td',
    'opponent_total_plays', 'opponent_total_yards', 'opponent_avg_yds',
    'opponent_pass_first_downs', 'opponent_rush_first_downs', 'opponent_first_down_pens', 'opponent_total_first_downs',
    'opponent_total_penalties', 'opponent_total_penalties_yds',
    'opponent_total_fum', 'opponent_total_int', 'opponent_total_to'
]

# Load the CSV file with updated headers
csv_file_path = ''
df = pd.read_csv(csv_file_path, names=column_names, header=0)

# Drop rows with any NaN values (like the header row if it gets included as data)
df.dropna(inplace=True)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="",
    port=4228,  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

try:
    for index, row in df.iterrows():
        try:
            # Insert the data directly into Defensive_Stats
            sql_query = """
                INSERT INTO Defensive_Stats (
                    date, opponent, location, result, opponent_passing_cmp, opponent_passing_att, opponent_completion_pct, 
                    opponent_passing_yds, opponent_passing_td, opponent_rushing_att, opponent_rushing_yds, opponent_rushing_avg, 
                    opponent_rushing_td, opponent_total_plays, opponent_total_yards, opponent_avg_yds, 
                    opponent_pass_first_downs, opponent_rush_first_downs, opponent_first_down_pens, opponent_total_first_downs, 
                    opponent_total_penalties, opponent_total_penalties_yds, opponent_total_fum, opponent_total_int, 
                    opponent_total_to
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(sql_query, (
                row['Date'], row['Opponent'], row['raw_location'], row['Result'],
                row['opponent_pass_cmp'], row['opponent_pass_att'], row['opponent_completion_pct'], row['opponent_pass_yds'], row['opponent_pass_td'],
                row['opponent_rush_att'], row['opponent_rush_yds'], row['opponent_rush_avg'], row['opponent_rush_td'],
                row['opponent_total_plays'], row['opponent_total_yards'], row['opponent_avg_yds'],
                row['opponent_pass_first_downs'], row['opponent_rush_first_downs'], row['opponent_first_down_pens'], row['opponent_total_first_downs'],
                row['opponent_total_penalties'], row['opponent_total_penalties_yds'],
                row['opponent_total_fum'], row['opponent_total_int'], row['opponent_total_to']
            ))

        except Exception as e:
            print("Error with row:", row.to_dict())
            print("Exception:", e)
            # Rollback the current transaction to avoid a deadlock situation
            conn.rollback()

    # Commit the transaction
    conn.commit()

except Exception as e:
    print("Transaction failed:", e)
    # Rollback the transaction if there is an error
    conn.rollback()

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()

print("Defensive data processing completed!")
