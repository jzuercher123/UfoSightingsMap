import csv
import json


coordinates = []
geoformat = {
    "type": "MultiPoint",
    'coordinates': coordinates
}


def get_lat_lng(file):
    coordinates = []
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
        for lat_lng in coordinates:
            write_file.write(f"{lat_lng}\n")


def csv_to_geojson():
    with open('../test_data/cleaned_sightings.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            coordinates.append([row[9], row[10]])
            print(f"row {row[9]} and {row[10]} appended")


get_lat_lng('../test_data/cleaned_sightings.csv')
