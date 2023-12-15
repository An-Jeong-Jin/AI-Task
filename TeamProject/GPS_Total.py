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
    
import requests
import googlemaps
import json
import re

center = [36.14527, 128.3918]

GOOGLE_API_KEY = "AIzaSyD1m-aX-rG5rf4DbIVBZCNYrnw9xRXa9YY"

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
data = {
    'considerIp': True, # 현 IP로 데이터 추출
}

result = requests.post(url, data).text # 해당 API에 요청을 보내며 데이터를 추출한다.

l = []

for i in result.split("\n"):
    if i.find("lat") != -1 or i.find("lng") != -1:
        l.append(float(re.sub("[^0-9.]", "", i)))

loc = find_point_with_condition(l, center)
