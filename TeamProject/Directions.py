import folium
import networkx as nx
from geopy.distance import geodesic

def find_closest_waypoints(coord, all_coords, num_closest=3):
    closest_waypoints = sorted(all_coords, key=lambda x: geodesic(coord, all_coords[x]).kilometers)[:num_closest]
    return closest_waypoints

coords = {
    'waypoint1':(36.14393, 128.3935),
    'waypoint02':(36.143805, 128.394),
    'waypoint03':(36.14354, 128.3932),
    'dz 옆문':(36.14578, 128.3926),
    'd 1층 도서관쪽':(36.14595, 128.3929),
    'end':(36.14621, 128.3926),
    'd 1층 기숙사쪽 뒷문':(36.14609, 128.392),
    'waypoint08':(36.14536, 128.3932),
    'waypoint09':(36.14534, 128.392838),
    'waypoint10':(36.14555, 128.39323),
    'waypoint11':(36.14597, 128.39316),
    'waypoint12':(36.14327, 128.39408),
    'waypoint13':(36.14329, 128.39348),
    'waypoint14':(36.14345, 128.39408),
    'waypoint15':(36.14376, 128.39416),
    'waypoint16':(36.14343, 128.39313),
    'waypoint17':(36.14465, 128.39226),
    'waypoint18':(36.14451, 128.39334),
    'waypoint19':(36.144907, 128.39327634),
    'waypoint20':(36.14364, 128.3928),
    'waypoint21':(36.1438, 128.39257),
    'waypoint22':(36.14425, 128.39238),
    'waypoint23':(36.14394, 128.39247),
    'waypoint24':(36.14531, 128.392068),
    'waypoint25':(36.145685, 128.392),
    'start':(36.14548, 128.3928),
    'waypoint27':(36.14311, 128.39374),
    'waypoint28':(36.14667, 128.39165),
    'waypoint29':(36.14667, 128.39155),
    'waypoint30':(36.14605, 128.39188)
}


roads = []


for point1, coord1 in coords.items():
    closest_waypoints = find_closest_waypoints(coord1, coords)
    for point2 in closest_waypoints:
        if point1 != point2:
            distance = geodesic(coord1, coords[point2]).kilometers
            roads.append((point1, point2, distance))


mymap = folium.Map(location=coords['start'], zoom_start=20)


G = nx.Graph()
for road in roads:
    start, end, distance = road
    G.add_edge(start, end, weight=distance)
shortest_path = nx.shortest_path(G, source='start', target='end', weight='weight')
print("Shortest Path:", shortest_path)

for i in range(len(shortest_path) - 1):
    start, end = shortest_path[i], shortest_path[i + 1]
    folium.PolyLine([coords[start], coords[end]], color="blue", weight=2.5, opacity=1).add_to(mymap)

mymap
