# FILE INFO: Use this file for all geojson data manipulation functions

import json
import geojson
from geojson import Point
from geojson import MultiPoint
import os
import re

# current directory
current_dir = os.getcwd()

# path to geojson/data test files directory
path_to_test_data = os.path.abspath("C:/Users/13096/PycharmProjects/flaskProject/data/test_data/")
geojson_filename = "\\geojson-points.geojson"
full_test_data_path = str(os.path.join(path_to_test_data + geojson_filename))

# class representing geojson objects of ufo sighting data (point, details, data_time)
class PointsClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def __geo_interface(self):
        return {'type': 'Point', 'coordinates': (self.x, self.y)}


def get_raw_coords() -> None:
    coord_list = []
    with (open(full_test_data_path, 'r') as file):
        for line in file.readlines():
            line = line.split()
            for word in line:
                results = re.findall(r"^((\-?|\+?)?\d+(\.\d+)?),\s*", word)
                print(str(results) + " found")
                coord_list.append(str(results))
    with open('../test_data/raw_data.txt', 'w') as rawdata_file:
        rawdata_file.write("\n".join(coord_list))
        rawdata_file.close()
    file.close()
    print("Done")


def clean_coords(raw_coords: list):
    coordinates_list = []
    if (str(raw_coords).isalnum() is True) and (raw_coords != 0):
        coordinates_list.append(raw_coords)
        print(str(raw_coords) + " added")
        return coordinates_list

def remove_whitespace():
    with open('../test_data/scrubbed.txt', 'w') as file:
        with open('../test_data/coordinates.txt', 'r') as f:
            lines = f.readlines()
            lines = [line for line in lines if line.strip()]
            for line in lines:
                print(line)
                file.write(line)
            f.close()
        file.close()

def clean():
    with open('../test_data/raw_data.txt', 'r') as f:
        lines = f.readlines()
        coordinates = [re.findall(r"[-+]?\d*\.\d+|\d+", line) for line in lines]
        with open('../test_data/coordinates.txt', 'w') as output_file:
            for coordinate in coordinates:
                coordinates = [coordinate for coordinate in coordinates if coordinate]
                print(coordinate)
                output_file.write(','.join(coordinate) + '\n')


def check_geojson_syntax(file_path):
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)

    validation_result = geojson.GeoJSON.check_list_errors(geojson_data)

    if validation_result["valid"] == "yes":
        print("The GeoJSON syntax is valid.")
    else:
        print("The GeoJSON syntax is invalid. Error: " + validation_result['message'])

check_geojson_syntax(full_test_data_path)