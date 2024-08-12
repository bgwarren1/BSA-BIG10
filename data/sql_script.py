import pandas as pd
import psycopg2

# Specify the column names, including 'Rk', which we'll ignore later
column_names = ['Rk', 'Date', 'raw_location', 'Opponent', 'Result']

# Load in data
csv_file_path = '/Users/blairwarren/Desktop/BSA Article/bsa-big10-predictive-analysis/data/oregon_game_logs.csv'
df = pd.read_csv(csv_file_path, names=column_names, header=0, usecols=['Date', 'raw_location', 'Opponent', 'Result'])

# Print out column names to confirm
print("Columns in the DataFrame:", df.columns)

# Connect to my PostgreSQL db
conn = psycopg2.connect(
    host="localhost",
    port=4228,  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# Iterate through the DataFrame and insert data into the staging table
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO Staging_Games (date, opponent, raw_location, result) VALUES (%s, %s, %s, %s)
        """,
        (row['Date'], row['Opponent'], row['raw_location'], row['Result'])
    )

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted!")
