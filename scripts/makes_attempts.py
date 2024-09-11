import pandas as pd
import psycopg2

df = pd.read_csv('')

# two new columns for FG_Makes and FG_Attempts with error handling
def parse_fg(fg_value):
    try:
        makes, attempts = fg_value.split('-')
        return int(makes), int(attempts)
    except (ValueError, IndexError):
        return None, None

df['FG_Makes'], df['FG_Attempts'] = zip(*df['FG'].apply(parse_fg))



conn = psycopg2.connect(
    host="",
    port="",  
    database="",  
    user="",  
    password=""  
)
cursor = conn.cursor()

# Update the table with FG_Makes and FG_Attempts
for index, row in df.iterrows():
    if row['FG_Makes'] is not None and row['FG_Attempts'] is not None:
        try:
            cursor.execute("""
                UPDATE UCLA_Kicking_Stats
                SET FG_Makes = %s,
                    FG_Attempts = %s
                WHERE date = %s AND opponent = %s AND location = %s;
            """, (
                row['FG_Makes'], row['FG_Attempts'], row['Date'], 
                row['Opponent'], row['raw_location']
            ))
        except Exception as e:
            print(f"Error with row: {row}")
            print(f"Exception: {e}")
            conn.rollback()


conn.commit()
cursor.close()
conn.close()

print("Data successfully updated!")
