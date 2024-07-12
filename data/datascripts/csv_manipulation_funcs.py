import csv
import json
from data.DatabaseHandler import DatabaseHandler

# global data
COORDINATES = []

def get_coordinates(file):
    COORDINATES = []
    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                lat_lng = [float(row[9]), float(row[10])]
                coordinates.append(lat_lng)
                print(str(str(float(row[9])) + ", " + str(float(row[10]))))
            except ValueError:
                pass
        write_file = open('../test_data/scrubbed.txt', 'w')
        for lat_lng in COORDINATES:
            write_file.write(f"{lat_lng}\n")


def csv_to_geojson():
    with open('../test_data/cleaned_sightings.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            COORDINATES.append([row[9], row[10]])
            print(f"row {row[9]} and {row[10]} appended")


def sql_table_to_csv(
        db_name: str,
        table_name: str,
        output_filename: str):
    print(f"-- Initializing {db_name}")
    db_handler = DatabaseHandler(db_name)

    print(f"-- Opening {output_filename}")
    with open(output_filename, 'w') as file:

        writer = csv.writer(file)
        table = db_handler.fetch_from_table(table_name=table_name)
        columns = db_handler.get_table_columns(table_name=table_name)
        writer.writerow(columns)
        print("-- Writing headers")
        for row in table:

            print(f"-- WRITING ROW")
            try:
                print(row)
            except Exception:
                pass
            writer.writerow(row)



sql_table_to_csv(db_name='../sightings.db', table_name='sightings', output_filename='../ufo_sightings/scrubbed.csv')
