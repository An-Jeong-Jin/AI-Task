####네이버 카페

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
i = []
user_id = input('naver_id:')
user_pw = input('naver_pw:')

browser = webdriver.Chrome() # 현재파일과 동일한 경로일 경우 생략 가능



# 1. 네이버 이동
browser.get('https://section.cafe.naver.com/ca-fe/home')

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.XPATH, '//*[@id="mainContainer"]/div[3]/div[1]/div/div[1]/a').click()

#네이버 아이디 입력
log_ID = browser.find_element(By.XPATH, value='//*[@id="id"]')
log_ID.click()
pyperclip.copy(user_id)
log_ID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

log_PID = browser.find_element(By.XPATH, value='//*[@id="pw"]')
log_PID.click()
pyperclip.copy(user_pw)
log_PID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
#### 굳이 pyperclip을 사용하는 이유는 이렇게 해서 복붙해주지 않으면 자동로그인 방지 문자가 떠서 굉장히 귀찮아 진다.
#3. id 복사 붙여넣기
# elem_id = browser.find_element(By.XPATH, '//*[@id="id_line"]').click()
# pyperclip.copy(user_id)
# elem_id.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)

# # # 4. pw 복사 붙여넣기
# elem_pw = browser.find_element(By.XPATH, '//*[@id="pw_line"]').click()
# pyperclip.copy(user_id)
# elem_pw.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)
# time.sleep(1)

# # 5. 로그인 버튼 클릭
browser.find_element(By.XPATH, value='//*[@id="log.login"]').click()

cafe_name_element = browser.find_element(By.XPATH, value = '//*[@id="mainContainer"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]')
cafe_name = cafe_name_element.text
print("크롤링 사이트:", cafe_name)

book_cafa_main = browser.find_element(By.XPATH, value = '//*[@id="mainContainer"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/a').click()

p = []
driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/readbook')
book_story_href = driver.find_element(By.XPATH, value = '//*[@id="menuLink357"]')

book_story_href = book_story_href.get_attribute('href')
print(book_story_href)

book_story_browser = webdriver.Chrome()
book_story_browser.get("https://cafe.naver.com/ArticleList.nhn?search.clubid=10004632&search.menuid=357&search.boardtype=L")

book_href_list = book_story_browser.find_element(By.CSS_SELECTOR, value = '#main-area > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a') 
print(book_href_list)
