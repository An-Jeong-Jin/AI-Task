import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/society#1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

newslist = soup.select(".list_newsmajor > li")  # 원하는 기사 요소에 접근

for news_item in newslist: 
    info_cp = news_item.select_one(".info_cp").text
    link_txt = news_item.select_one(".link_txt")['href']
    title = news_item.select_one(".link_txt").text.strip() 
    
    print("언론사:", info_cp)
    print("뉴스 제목:", title)
    print("뉴스 링크:", link_txt)
    print("")
