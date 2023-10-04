# crawling-final

#공부하면서 만든 크롤링 코드

-crawling - 다음 뉴스 중 사회 뉴스 기사를 크롤링

crawling2 - 무신사의 인기있는 청바지를 순위별로 크롤링

crawling-final - 청바지만을 크롤링하는 crwaling2를 보안하고 발전시켜 여러 카테고리별 제품들을 순위별로 크롤링

# 주제 
옷에 관심이 많아 무신사 웹의 청바지를 크롤링 해주는 코드를 만들었고 이 과정에서 청바지외의 여러 옷들을 불러오는 카테고리별 크롤링 프로그램을 만들고 여러 옷들의 다양한 정보를 공유하고 싶어 주제로 선정하였다.


* * *
# 내가 공부한 크롤링 기법

1.BeautifulSoup - 웹 스크래핑에서 HTML과 XML문서를 파싱하고 데이터를 추출하기 위해 사용한 라이브러리이다. 이를 이용해 BeautifulSoup를 사용하기 위해 HTML을 파싱하여 객체를 생성하고 이 생성된 BeautifulSoup 객체를 사용하여 웹 페이지 내의 원하는 정보가 담긴 태그, 요소를 선택하여 원하는 정보 및 텍스트를 추출. 이를 통해 HTML과 같은 웹의 구조를 이해하고 웹에서의 정보를 추출하고 가공하여 데이터를 가져오는 과정에 큰 도움이 되었다. 또한 인터넷과 책을 참고하며 사용하다는 과정에서 쉽게 이해할 수 있고 친숙하게 다룰 수 있어서 좋았다.


2.Selenium - 각각의 카테고리별 링크를 불러오는 과정에서 BeautifulSoup을 이용했지만 아래에서 볼 수 있듯이 여러 오류로 인해 정적 웹 페이지 임에도 이러한 오류와 문제들을 해결하기 위해 사용한 라이브러리이다. 웹 브라우저의 드라이버에 접속하며 제어하며 웹 페이지의 동작을 모방하고 원하는 데이터를 추출하는데 사용하였다. 실제 웹 브라우저를 제어하면서 웹 페이지의 동작을 모방하며 원하는 데이터를 추출하는데 효과적이어서 필요한 웹 데이터들이 가려져있는 동적 웹 페이지에 효과적으로 사용가능하다. 비록 동적인 웹 페이지에서 원하는 웹 데이터를 추출해서 사용한건 아니지만 Selenium을 사용하는 과정에서 개념과 작동원리에 대해 공부할 수 있었고 Selenium을 통해 웹에 들어가 자동으로 데이터를 추출하는 과정이 흥미롭게 느껴져 재미있게 다룬 라이브러리이다.


3.lxml, html.paser - lxml과 html.paser은 문서를 파싱(구문 분석 및 변환)하고 처리하는데 사용되는 라이브러리 도구로 lxml을 통해 복잡한 문서를 파싱하고 데이터를 추출하는데 사용하였다. 이를 통해 웹 데이터를 수집하고 분석하는데 필요한 라이브러리와 도구에 대한 이해도를 높일 수 있었다.




* * *


# 코드 오류 및 수정 과정

1.HTTP 404에러 & 빈 리스트(데이터가 불러와지지 않는 오류)
정적 웹사이트인 무신사에서 BeautifulSoup를 이용해 카테고리를 데이터를 긁어오려하자 다음과 같은 403에러 발생
    
    HTTPError: HTTP Error 403: Forbidden

    [https://soy3on.tistory.com/185](https://studyingengineer.tistory.com/1040)과 같은 사이트를 참고하여 403 에러의 오류를 잡았으나 긁어올려하는 데이터가 수집되지 않고 []와 같은 빈리스트로 출력되는 문제 발생

해결방법 -  BeautifulSoup 대신 새로운 방법인 Selenium을 사용하여 해당 부분의 select에서 추가로 li와 a태그에 접근하여 각각의 카테고리별 href 링크를 가져옴
    
    import pandas as pd                                           #수정 후
    from tabulate import tabulate
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import requests
    from bs4 import BeautifulSoup
    
    driver = webdriver.Chrome()
    driver.get('https://www.musinsa.com/app/')
    
    li = []
    items = drive법 - 변수에 값을 할당하고 변수를 반환하며 None값이 출력되는 문제를 해결하였고 if문을 통해 원가만 뜨는 경우와 원가와 할인가격이 뜨는 경우를 나누어 최저금액이 뜨도록 설정

          for item in denim_pants:                                                                #수정 후
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

* * *
 
# 문제를 해결하며 

1. selenium을 사용하여 찾은 가장 인기있는 옷과 가방과 같은 인기 상품의 카테고리별 링크 각각 추출 

2. 추출한 링크로 접속해 BeautifulSoup을 이용해 인기 순위별 제품을 차례대로 크롤링 

3. 크롤링한 정보를 판다스와 tabulate 라이브러리를 통해 표로 정리하여 니트, 가디건, 슬랙스 등과 같은 여러 카테고리별 물건을 인기 순위별로 나타내었다.


* * *

# 코드 실행 결과
<img width="981" alt="image" src="https://github.com/An-Jeong-Jin/crawling-final/assets/120768669/c0d7568c-7c8a-42a9-8311-2a2452e82a7d">

여러 카테고리중 원하는 옷/물건을 입력했을때 순위별로 해당 옷/물건의 제품이름, 가격, 이미지, 링크를 크롤링하여 표로 나타낸다.

해당 코드는 니트를 입력한 예시


* * *

# 코드 설명

코드내에 주석처리로 코드 설명

