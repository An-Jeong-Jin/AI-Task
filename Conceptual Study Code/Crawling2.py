 import requests
from bs4 import BeautifulSoup

url = "https://www.musinsa.com/categories/item/003002?d_cat_cd=003002&brand=&list_kind=small&sort=sale_high&sub_sort=1m&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

denim_pants = soup.select(".li_box") #무신사 웹에서 li_box 클래스를 가진 모든 html 요소 선택
data_list = []

for item in denim_pants:
    name = item.select_one(".list_info a").text.strip() #각각의 제품의 이름을 .list_info a 선택자로 찾고 텍스트로 추출
    price = item.select_one(".price").text.strip().split()  
    image_link = item.select_one(".list_img img")['data-original']
    site_link = item.select_one(".list_img a")['href']

    data_list.append({ 'Name': name, 'Price': price, 'Image Link': image_link, 'Site Link': site_link})

for data in data_list[:5]:
    print("제품:", data['Name'])
    print("할인가격:", data['Price'][1])
    print("이미지:", data['Image Link'])
    print("링크:", data['Site Link'])
    print("")                   
