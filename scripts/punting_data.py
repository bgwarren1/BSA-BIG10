import pandas as pd
import psycopg2

# Column names for the dataset
column_names = [
    'Rk', 'Date', 'raw_location', 'Opponent', 'Result', 
    'Punts', 'Yds', 'Avg'
]


csv_file_path = ''  
df = pd.read_csv(csv_file_path, names=column_names, header=0)

# Ensure that date is interpreted as a string
df['Date'] = df['Date'].astype(str)


print(df.head())


conn = psycopg2.connect(
    host="",
    # port = ,  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# SQL query to insert data into Punting_Stats table
sql_query = """
    INSERT INTO Oregon_Punting_Stats (
        date, raw_location, opponent, result, punts, yds, avg
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Loop through the DataFrame and insert each row into the database
for index, row in df.iterrows():
    try:
        cursor.execute(sql_query, (
            row['Date'], row['raw_location'], row['Opponent'], row['Result'], 
            row['Punts'], row['Yds'], row['Avg']
        ))
    except Exception as e:
        print(f"Error inserting row {index}: {e}")
        conn.rollback()  # Rollback the transaction if an error occurs
        break  # Stop the loop if a rollback is triggered

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Punting data processing completed!")
