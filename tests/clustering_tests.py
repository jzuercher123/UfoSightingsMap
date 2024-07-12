import folium
import csv
from folium.plugins import MarkerCluster
from data.DatabaseHandler import DatabaseHandler

db_handler = DatabaseHandler('../data/sightings.db')

# Change the '<correct_file_path>' to the actual path of scrubbed.txt
with open('../data/ufo_sightings/scrubbed.csv', 'r') as file:
    sighting_data = []
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        try:
            print(line)
            sighting_data.append(line)
        except ValueError:
            pass
    
    """
    for line in file:
        transformed_items = [item.replace('[', "").replace(']', "") for item in line.strip().split(',')[:2]]
        try:
            if len(sighting_data) > 1:
                print(sighting_data[1])
                map_coordinate = {'lat': float(transformed_items[0]), 'lon': float(transformed_items[1]),
                                  'popup': 'data'}
            print(map_coordinate)
        except ValueError:
            pass
        random_coordinates.append(transformed_items)"""

    # Create a map centered around the global
m = folium.Map(location=[0, 0], zoom_start=2)

# Create a MarkerCluster element and add it to the map
marker_cluster = MarkerCluster().add_to(m)

# Add each coordinate pair to the MarkerCluster element
i = 0
for data in sighting_data:
    print(str(i))
    if len(data) >=3:
        try:
            description = data[1]
            coordinates = (float(data[2]), float(data[3])) # lat and lng
            html = f'{description}'
            iframe = folium.IFrame(html,
                                   width=100,
                                   height=100)
            folium.Marker(
                location=coordinates,
                popup=folium.Popup(iframe, max_width=100)
            ).add_to(marker_cluster)
            i = i + 1
            if i >= 70000:
                break
        except IndexError:
            i = i + 1
            break



# Save the map to an HTML file
m.save('marker_cluster.html')