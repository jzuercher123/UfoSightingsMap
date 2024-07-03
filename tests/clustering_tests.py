import folium
from folium.plugins import MarkerCluster

# Change the '<correct_file_path>' to the actual path of scrubbed.txt
with open('../data/scrubbed.txt', 'r') as file:
    random_coordinates = []
    for line in file:
        transformed_items = [item.replace('[', "").replace(']', "") for item in line.strip().split(',')[:2]]
        try:
            map_coordinate = {'lat': float(transformed_items[0]), 'lon': float(transformed_items[1]),
                              'popup': 'This is the middle of the map.'}
            print(map_coordinate)
        except ValueError:
            pass
        random_coordinates.append(transformed_items)

    # Create a map centered around the global
m = folium.Map(location=[0, 0], zoom_start=2)

# Create a MarkerCluster element and add it to the map
marker_cluster = MarkerCluster().add_to(m)

# Add each coordinate pair to the MarkerCluster element
for coords in random_coordinates:
    folium.CircleMarker(location=coords).add_to(marker_cluster)

# Save the map to an HTML file
m.save('marker_cluster.html')