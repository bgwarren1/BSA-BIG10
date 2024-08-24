import pandas as pd
import psycopg2

# Load the drops data
drops_df = pd.read_csv('/Users/blairwarren/Desktop/BSA Article/bsa-big10-predictive-analysis/data/oregon_drops.csv')

# Fill NaN drops with 0 and convert to integers
drops_df['Drops'] = drops_df['Drops'].fillna(0).astype(int)

# Reconnect to database
conn = psycopg2.connect(
    host="localhost",
    port="4228",  
    database="postgres",  
    user="postgres",  
    password="Blairp11"  
)
cursor = conn.cursor()

# Update the table with drops data
for index, row in drops_df.iterrows():
    try:
        # Print the SQL command for debugging
        print(f"Updating: Date={row['Date']}, Opponent={row['Opponent']}, Location={row['raw_location']}, Drops={row['Drops']}")
        
        cursor.execute("""
            UPDATE Oregon_Offensive_Stats
            SET Drops = %s
            WHERE date = %s AND opponent = %s AND raw_location = %s;
        """, (
            row['Drops'], row['Date'], row['Opponent'], row['raw_location']
        ))

    except Exception as e:
        print(f"Error with row: {row}")
        print(f"Exception: {e}")
        conn.rollback()

conn.commit()
cursor.close()
conn.close()

print("Drops data successfully inserted!")
