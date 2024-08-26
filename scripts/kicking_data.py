import pandas as pd
import psycopg2

# Column names for the dataset
column_names = [
    'Rk', 'Date', 'raw_location', 'Opponent', 'Result', 
    '1-19', '20-29', '30-39', '40-49', '50+', 'LNG', 
    'FG%', 'FG', 'XP', 'PTS'
]

# Load the CSV file with specified headers
csv_file_path = '/Users/blairwarren/Desktop/BSA Article/bsa-big10-predictive-analysis/data/USCKickingData.csv'
df = pd.read_csv(csv_file_path, names=column_names, header=0)

# Function to handle FG ranges (e.g., '0-0') and convert them to the number of successful FGs
def convert_fg_value(value):
    try:
        made, _ = map(int, value.split('-'))
        return made
    except ValueError:
        return 0

# Apply the conversion function to the relevant columns
df['1-19'] = df['1-19'].apply(convert_fg_value)
df['20-29'] = df['20-29'].apply(convert_fg_value)
df['30-39'] = df['30-39'].apply(convert_fg_value)
df['40-49'] = df['40-49'].apply(convert_fg_value)
df['50+'] = df['50+'].apply(convert_fg_value)
df['FG'] = df['FG'].apply(convert_fg_value)

# Handle the XP column, similar to the FG columns
df['XP'] = df['XP'].apply(convert_fg_value)

# Convert the LNG column to integers
df['LNG'] = pd.to_numeric(df['LNG'], errors='coerce').fillna(0).astype(int)

# Fill FG% with 0 if NaN and ensure it's a float
df['FG%'] = df['FG%'].fillna(0).astype(float)

# Handle NaN or missing values in PTS
df['PTS'] = df['PTS'].fillna(0).astype(int)

# Connect to database
conn = psycopg2.connect(
    host="",
    # port =   
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

for index, row in df.iterrows():
    try:
        # Insert the data into the Kicking_Stats table
        sql_query = """
            INSERT INTO Kicking_Stats (
                date, opponent, location, result, fg_1_19, fg_20_29, fg_30_39, fg_40_49, fg_50_plus, longest_fg,
                fg_percentage, fg_made, xp_made, points_scored
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql_query, (
            row['Date'], row['Opponent'], row['raw_location'], row['Result'],
            row['1-19'], row['20-29'], row['30-39'], row['40-49'], row['50+'], row['LNG'],
            row['FG%'], row['FG'], row['XP'], row['PTS']
        ))

    except Exception as e:
        print("Error with row:", row.to_dict())
        print("Exception:", e)
        conn.rollback()  


conn.commit()
cursor.close()
conn.close()

print("Kicking data successfully inserted!")
