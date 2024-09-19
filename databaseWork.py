import sqlite3
import pandas as pd

# Load the CSV file into a pandas DataFrame
csv_file = 'FYA_World_Class.csv'
df = pd.read_csv(csv_file)


##conn = sqlite3.connect('attractions.db')
##
##c = conn.cursor()
##
##c.execute('''
##CREATE TABLE IF NOT EXISTS attractions (
##    id INTEGER PRIMARY KEY,
##    attraction TEXT,
##    guest TEXT,
##    avg_tourist_test TEXT,
##    leslie_stahl_test TEXT,
##    smartphone_test TEXT,
##    tony_stark_test TEXT,
##    hollywood_test TEXT,
##    simpsons_test TEXT,
##    signature_moment TEXT,
##    premature_detractulation TEXT,
##    exit_hall_test TEXT,
##    fine_wine TEXT,
##    score INTEGER,
##    world_class TEXT
##)
##''')
##
##c.close()
### Insert data from the DataFrame into the SQLite table
##df.to_sql('attractions', conn, if_exists='append', index=False)
##
### Commit and close the connection
##conn.commit()
###conn.close()
##
##print("Data successfully inserted into SQLite database!")
