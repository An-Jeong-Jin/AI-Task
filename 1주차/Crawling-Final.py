import pandas as pd
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests  #HTTP 요청을 보내고 웹 서버와 상호작용하기 위해 사용
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  
driver.get('https://www.musinsa.com/app/')  #selenium을 사용하여 무신사 스토어 웹사이트에 접속

li = []
items = driver.find_elements(By.CSS_SELECTOR, '#leftCommonPc > div > section.sc-g0sulw-0.bvYiGx > div:nth-child(2) > nav > div:nth-child(1) > div.sc-8hpehb-7.liOFHO > ul > li > a')
#웹 페이지에서 카테고리 링크를 찾아 li 리스트에 저장
for i in items:   
    li.append(i.get_attribute("href"))

def Musinsa(t):  #Musinsa 함수를 정의하고 입력한 카테고리에 대한 정보를 웹에서 스크랩 및 결과 반환
    T = {"맨투맨": li[0], "스웨트셔츠": li[0], "니트": li[1], "스웨터": li[1], "셔츠": li[2], "블라우스": li[2], "트레이닝 팬츠": li[3], "조거 팬츠": li[3], "후드": li[4], "티셔츠": li[4], "캡 모자": li[5], "야구 모자": li[5], "데님 팬츠": li[6], "가디건": li[7], "코튼 팬츠": li[8], "숄더백": li[9], "슈트 팬츠": li[10], "슬랙스": li[10], "메신저 백": li[11], "크로스 백": li[11], "백팩": li[12], "캔버스": li[13], "단화": li[13], "패션스니커즈화": li[14], "블루종": li[15], "MA-1": li[15]}
    if t in T:
        a = T[t]
    else:
        return "해당 카테고리는 존재하지 않습니다"  #해당 카테고리가 없을 시 "해당 카테고리는 존재하지 않습니다" 반환

    url = a  # 해당 카테고리 페이지에 접속하여 데이터를 스크랩
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'} #일반적인 브라우로부터의 요청으로 인식되게 하기 위
    res = requests.get(url, headers=headers)         #설정한 url로 HTTP GET요청 및 웹 페이지의 내용 받아옴 headers 정보를 함께 전송하여 웹 서버로부터 응답을 받을 때, 사용자 에이전트 정보가 포함되어 있다고 인식되도록 함  
    soup = BeautifulSoup(res.text, 'lxml')          #받아온 웹 페이지의 HTML 내용을 파싱하고 파싱된 결과를 soup에 저장 lxml 파서를 사용하여 HTML문서를 파싱하여 soup객체를 통한 다양한 요소 선택 및 데이터 추출 가능

    denim_pants = soup.select(".li_box") # 스크랩한 데이터 가공 및 리스트에 저장
    data_list = []

    for item in denim_pants:                                     #웹 페이지에서 각각의 요소에 할당하는 값을 정보 추출 및 텍스트 변경
        name = item.select_one(".list_info a").text.strip().replace(" ", "")
        price = item.select_one(".price").text.strip().split()
        image_link = item.select_one(".list_img img")['data-original']
        site_link = item.select_one(".list_img a")['href']
        data_list.append({'Name': name, 'Price': price, 'Image Link': image_link, 'Site Link': site_link})

    result = []
    for data in data_list[:20]:
        t = {
            '제품': data['Name'],
            '가격': data['Price'][1] if len(data['Price']) >= 2 else data['Price'][0],
            '이미지': data['Image Link'],
            '링크': data['Site Link']
        }
        result.append(t)

    return result

user_input = input()
result = Musinsa(user_input)
if isinstance(result, list) and len(result) > 0:       #변수가 리스트인지 확인 및 데이터가 비어있지 않은지 확인
    df = pd.DataFrame(result)                          #리스트면서 데이터가 있으면 판다스 데이터 프레임으로 변환     
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
else:
    print(result)                                      #그렇지 않으면 result 출력
                                                       # 해당 하지 않은 카테고리를 입력할때 "해당 카테고리는 존재하지 않습니다"라는 출력값을 고려하여 조건문을 사용

driver.quit()
