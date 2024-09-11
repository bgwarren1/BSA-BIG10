import psycopg2
import pandas as pd

# Connect to database
conn = psycopg2.connect(
    host="",
    port='',  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()


cursor.execute("SELECT * FROM Offensive_Stats")

# Fetch all the data returned by the query
rows = cursor.fetchall()

# Get the column names from the cursor description
columns = [desc[0] for desc in cursor.description]

# Convert the data to df
df = pd.DataFrame(rows, columns=columns)

# Close
cursor.close()
conn.close()

# Display
print(df)
