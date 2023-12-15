import requests
import googlemaps
import json

GOOGLE_API_KEY = "AIzaSyD1m-aX-rG5rf4DbIVBZCNYrnw9xRXa9YY"
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
data = {
    'considerIp': True, # 현 IP로 데이터 추출
}

result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

print(result.text)
