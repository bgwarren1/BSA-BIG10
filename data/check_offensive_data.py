import psycopg2
import pandas as pd

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=4228,  
    database="postgres",  
    user="postgres",  
    password="Blairp11"  
)
cursor = conn.cursor()

# Execute a query to select all data from the Offensive_Stats table
cursor.execute("SELECT * FROM Offensive_Stats")

# Fetch all the data returned by the query
rows = cursor.fetchall()

# Get the column names from the cursor description
columns = [desc[0] for desc in cursor.description]

# Convert the data to a pandas DataFrame for easy viewing
df = pd.DataFrame(rows, columns=columns)

# Close the connection
cursor.close()
conn.close()

# Display the DataFrame
print(df)
