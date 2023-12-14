import folium
import networkx as nx
import math
import time
from IPython.display import display, clear_output    # 이미지, 그래프 표시시
import requests        #Google Maps Geolocation API에 대한 요청
import re


def find_point_with_condition(point_A, point_B, ratio=0.8):  ##point_A = gps, point_B= center 
    if point_A[0] > point_B[0] and point_A[1] < point_B[1]:    ## 위, 왼
        new_point_A = (                                          
            point_A[0] - ratio * (point_A[0] - point_B[0]),
            point_A[1] + ratio * (point_B[1] - point_A[1])
        )
    elif point_A[0] > point_B[0]:                            ## 위, 오
        new_point_A = (
            point_A[0] - ratio * (point_A[0] - point_B[0]),
            point_A[1] - ratio * (point_A[1] - point_B[1])
        )
    elif point_A[0] < point_B[0] and point_A[1] > point_B[1]:        ## 아래 ,오
        new_point_A = (
            point_A[0] + ratio * (point_B[0] - point_A[0]),
            point_A[1] - ratio * (point_A[1] - point_B[1])
        )
    else:                                                             ## 아래 , 왼
        new_point_A = (
            point_A[0] + ratio * (point_B[0] - point_A[0]),
            point_A[1] + ratio * (point_B[1] - point_A[1])
        )
    return new_point_A

def get_geolocation():
    coordinates = {
    1: (36.14393, 128.3935),
    2: (36.143805, 128.394),
    3: (36.14354, 128.3932),
    "db_3": (36.14578, 128.3926),
    "d1_1": (36.14595, 128.3929),
    "d1_2": (36.14621, 128.3926),
    "d1_3": (36.14609, 128.392),
    8: (36.14536, 128.3932),
    9: (36.14534, 128.392838),
    10: (36.14555, 128.39323),
    11: (36.14597, 128.39316),
    12: (36.14327, 128.39408),
    13: (36.14329, 128.39348),
    14: (36.14345, 128.39408),
    15: (36.14376, 128.39416),
    16: (36.14343, 128.39313),
    17: (36.14465, 128.39226),
    18: (36.14451, 128.39334),
    19: (36.144907, 128.39327634),
    20: (36.14364, 128.3928),
    21: (36.1438, 128.39257),
    22: (36.14425, 128.39238),
    23: (36.14394, 128.39247),
    24: (36.14531, 128.392068),
    25: (36.145685, 128.392),
    "db_2": (36.14548, 128.3928),
    27: (36.14311, 128.39374),
    28: (36.14667, 128.39165),
    29: (36.14667, 128.39155),
    30: (36.14605, 128.39188),
    31: (36.14620, 128.3924),
    32: (36.14628, 128.3931),
    33: (36.14613, 128.393155),
    34: (36.14626, 128.3929),
    35: (36.14571, 128.3923),
    36: (36.145685, 128.392),
    37: (36.14571, 128.3923),
    38: (36.14531, 128.392508),
    39: (36.14531, 128.392400),
    40 : (36.14498, 128.3922),
    41 :(36.14558, 128.3920),
    "db_1": (36.14558, 128.3922),
    43: (36.14566, 128.3921),
    44: (36.14360, 128.3941),
    45: (36.14372, 128.3942),
    46: (36.14335, 128.3933),
    47: (36.14359, 128.3930)
   
    }
    center = [36.14540, 128.3916]
    GOOGLE_API_KEY = "AIzaSyD1m-aX-rG5rf4DbIVBZCNYrnw9xRXa9YY"
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {'considerIp': True}
    result = requests.post(url, data).text
    gps = [float(re.sub("[^0-9.]", "", i)) for i in result.split("\n") if "lat" in i or "lng" in i]
    gps_node = find_point_with_condition(gps, center)
    min_distance = float('inf')
    closest_node = None
    for node, coord in coordinates.items():
        distance = math.sqrt((gps_node[0] - coord[0])**2 + (gps_node[1] - coord[1])**2)
        if distance < min_distance:
            min_distance = distance
            closest_node = node
    return closest_node

def direction(start_node, end_node):
    coordinates = {
    1: (36.14393, 128.3935),
    2: (36.143805, 128.394),
    3: (36.14354, 128.3932),
    "db_3": (36.14578, 128.3926),
    "d1_1": (36.14595, 128.3929),
    "d1_2": (36.14621, 128.3926),
    "d1_3": (36.14609, 128.392),
    8: (36.14536, 128.3932),
    9: (36.14534, 128.392838),
    10: (36.14555, 128.39323),
    11: (36.14597, 128.39316),
    12: (36.14327, 128.39408),
    13: (36.14329, 128.39348),
    14: (36.14345, 128.39408),
    15: (36.14376, 128.39416),
    16: (36.14343, 128.39313),
    17: (36.14465, 128.39226),
    18: (36.14451, 128.39334),
    19: (36.144907, 128.39327634),
    20: (36.14364, 128.3928),
    21: (36.1438, 128.39257),
    22: (36.14425, 128.39238),
    23: (36.14394, 128.39247),
    24: (36.14531, 128.392068),
    25: (36.145685, 128.392),
    "db_2": (36.14548, 128.3928),
    27: (36.14311, 128.39374),
    28: (36.14667, 128.39165),
    29: (36.14667, 128.39155),
    30: (36.14605, 128.39188),
    31: (36.14620, 128.3924),
    32: (36.14628, 128.3931),
    33: (36.14613, 128.393155),
    34: (36.14626, 128.3929),
    35: (36.14571, 128.3923),
    36: (36.145685, 128.392),
    37: (36.14571, 128.3923),
    38: (36.14531, 128.392508),
    39: (36.14531, 128.392400),
    40 : (36.14498, 128.3922),
    41 :(36.14558, 128.3920),
    "db_1": (36.14558, 128.3922),
    43: (36.14566, 128.3921),
    44: (36.14360, 128.3941),
    45: (36.14372, 128.3942),
    46: (36.14335, 128.3933),
    47: (36.14359, 128.3930)
   
    }


    # 그래프 생성
    G = nx.Graph()

    # 노드 추가
    for node, coord in coordinates.items():
        G.add_node(node, pos=coord)

    # 각 노드에 대해 가장 가까운 두 개의 이웃 찾기
    for node1 in G.nodes:
        distances = [
            (node2, math.sqrt((coordinates[node1][0] - coordinates[node2][0]) ** 2 + (coordinates[node1][1] - coordinates[node2][1]) ** 2))
            for node2 in G.nodes if node1 != node2
        ]
        closest_neighbors = sorted(distances, key=lambda x: x[1])[:2]
        for neighbor, distance in closest_neighbors:
            # 해당 좌표들끼리의 간선을 추가하지 않도록 조건 추가
            if node1 not in [4, 5, 6, 25, 26, 35,7, 38,24 ,42] or neighbor not in [4, 5, 6, 7,25, 26, 35, 38,24, 42]:
                if not ((node1 == 43 and neighbor == "d1_3") or (node1 == 24 and neighbor == "db_1")):
                    G.add_edge(node1, neighbor, weight=distance)
    # 최단 경로 찾기
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

    # 중심 좌표 계산
    center_lat, center_lon = sum(coord[0] for coord in coordinates.values()) / len(coordinates), sum(coord[1] for coord in coordinates.values()) / len(coordinates)
    mymap = folium.Map(location=[center_lat, center_lon], zoom_start=15)

    # 그래프 엣지에 회색 라인 추가
    for edge in G.edges:
        node1, node2 = edge
        folium.PolyLine([coordinates[node1], coordinates[node2]], color="gray", weight=2, opacity=0.5).add_to(mymap)
    
    for node, coord in coordinates.items():
        
        folium.Marker(
        location=coord,
        popup=f"노드: {node}",
        icon=folium.Icon(color='blue')
    ).add_to(mymap)
    
    # 최단 경로에 파란 라인 추가
    for i in range(len(shortest_path) - 1):
        node1, node2 = shortest_path[i], shortest_path[i + 1]
        folium.PolyLine([coordinates[node1], coordinates[node2]], color="blue", weight=2.5).add_to(mymap)
    # 출발 노드를 빨 간 마커로 표시
    folium.Marker(
    location=coordinates[start_node],
    popup=f"출발 노드: {start_node}",
    icon=folium.Icon(color='red')
    ).add_to(mymap)

    # 도착 노드를 초록 마커로 표시
    folium.Marker(
    location=coordinates[end_node],
    popup=f"도착 노드: {end_node}",
    icon=folium.Icon(color='green')
    ).add_to(mymap)
    
    # 지도를 HTML 파일로 저장
    display(mymap)
