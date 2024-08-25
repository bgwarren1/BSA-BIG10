import pandas as pd
import psycopg2

# Insert whichever csv needed
csv_file_path = ''
df = pd.read_csv(csv_file_path)

# Convert to string and remove commas, then we'll convert to float
df['Altitude'] = df['Altitude'].astype(str).str.replace(',', '').astype(float)
df['Distance'] = df['Distance'].astype(str).str.replace(',', '').astype(float)

# Convert other columns to appropriate data types if needed
df['Temp (F)'] = df['Temp (F)'].astype(float)
df['Precipitation (in)'] = df['Precipitation (in)'].astype(float)
df['Windspeed (mph)'] = df['Windspeed (mph)'].astype(float)

# connect to database
conn = psycopg2.connect(
    host="",
    port="",  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# Update the table with data from the CSV
for index, row in df.iterrows():
    try:
        cursor.execute("""
            UPDATE USC_Kicking_Stats
            SET temp_f = %s,
                precipitation_in = %s,
                windspeed_mph = %s,
                altitude_m = %s,
                distance_from = %s
            WHERE date = %s AND opponent = %s AND location = %s;
        """, (
            row['Temp (F)'], row['Precipitation (in)'], row['Windspeed (mph)'], 
            row['Altitude'], row['Distance'], row['Date'], 
            row['Opponent'], row['raw_location']  
        ))
        # Debugging using exceptions, which will give us the entry causing error
    except Exception as e:
        print(f"Error with row: {row}")
        print(f"Exception: {e}")
        conn.rollback()

# commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted!")
