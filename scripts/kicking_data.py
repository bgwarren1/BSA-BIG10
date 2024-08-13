import pandas as pd
import psycopg2
import numpy as np

# Column names for the dataset
column_names = [
    'Rk', 'Date', 'raw_location', 'Opponent', 'Result', 
    '1-19', '20-29', '30-39', '40-49', '50+', 'LNG', 
    'FG%', 'FG', 'XP', 'PTS'
]

# Load the CSV file
csv_file_path = ''
df = pd.read_csv(csv_file_path, names=column_names, header=0)

# Drop rows with any NaN values (like the header row if it gets included as data)
df.dropna(how='all', inplace=True)

# Handle NaN values specifically for the fields where they may appear
df.replace({np.nan: None}, inplace=True)

# Correct the data type for specific fields
df['LNG'] = df['LNG'].astype(float).fillna(0).astype(int)
df['FG%'] = df['FG%'].astype(float).fillna(0)
df['1-19'] = df['1-19'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['20-29'] = df['20-29'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['30-39'] = df['30-39'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['40-49'] = df['40-49'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['50+'] = df['50+'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['FG'] = df['FG'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)
df['XP'] = df['XP'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) else x)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="",
    # port = 
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# Insert the data into the Kicking_Stats table
for index, row in df.iterrows():
    try:
        sql_query = """
            INSERT INTO Kicking_Stats (
                date, opponent, location, result, fg_1_19, fg_20_29, fg_30_39, fg_40_49, fg_50_plus, 
                longest_fg, fg_percentage, fg_made, xp_made, points_scored
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql_query, (
            row['Date'], row['Opponent'], row['raw_location'], row['Result'],
            row['1-19'], row['20-29'], row['30-39'], row['40-49'], row['50+'], 
            row['LNG'], row['FG%'], row['FG'], row['XP'], row['PTS']
        ))

    except Exception as e:
        print("Error with row:", row.to_dict())
        print("Exception:", e)

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Kicking data successfully inserted!")
