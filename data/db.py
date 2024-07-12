import DatabaseHandler
import csv

# globals
TABLE_NAME = "sightings"
COLUMNS = """id INTEGER PRIMARY KEY, description TEXT, latitude FLOAT, longitude FLOAT"""

# initialize database handler
print("-- Initializing db : sightings.db")
db_handler = DatabaseHandler.DatabaseHandler('sightings.db')
print(f"-- Creating table {TABLE_NAME} with {COLUMNS}")
db_handler.create_table(table_name=TABLE_NAME, columns=COLUMNS)

# read csv rows, insert for each row :
# row[7], row[9], row[10] to 'sightings'
# table in sightings.db
with open('test_data/cleaned_sightings.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    i = 0
    for row in reader:
        i = i + 1
        try:
            db_row = (i, f'{row[7]}', f'{float(row[9])}', f'{float(row[10])}')
            print(f"-- Insterting {str(db_row)}")
            db_handler.insert_into_table('sightings', db_row)
        except Exception as e:
            continue
    print("!!-- Finished!!")

