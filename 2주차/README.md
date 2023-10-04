# Pretreatment-final

* * *

# 공부하면서 만든 전처리 코드

Pretreatment - 개념을 공부할 때 만들어 본 코드로 깃허브의 -crawling 코드를 변형하여 사회 뉴스의 각 텍스트들을 크롤링 및 토큰화, 불용어 처리, 명사 추출을 통한 전처리 코드
Pretreatment-final - 기존의 Pretreatment코드를 보완하고 발전시켜 사회뉴스뿐만 아니라 정치, 경제, 문화와 같은 여러 카테고리별 뉴스를 선택하여 각 뉴스의 텍스트들을 전처리하고 단어의 빈도수가 높은 순서대로 워드 클라우드로 나타낸 코드


# 주제 
다음 뉴스의 각 카테고리별 주제들을 선택하여 선택한 뉴스들의 텍스트 크롤링 및 선택한 뉴스의 중요단어 전처리 및 워드 클라우드로 시각화


* * *

# 내가 공부한 전처리 기법


1.토큰화 - 텍스트를 작은 단위로 나누는 과정으로 NLTK 라이브러리를 통해 크롤링하여 가져온 텍스트들을 단어로 나눔

2.불용어 처리 - 텍스트에서 제거해도 의미에 큰 영향을 주지 않는 불용어들을 제거하는 과정으로 NLTK 라이브러리를 통해 불용어 목록을 활용하여 필요없는 단어들을 제거

3.명사 추출 - 텍스트에서 명사만 추출하는 과정으로 konlpy 라이브러리의 형태소 분석기 중 하나인 Okt, Komoran, Hannanum중 Okt를 통해 불용어 처리를 마친 텍스트들에서 명사를 추출

4.워드 클라우드 시각화 - 텍스트를 시각적으로 나타내는 방법 중 하나이며 wordcloud 라이브러리를 통해 명사 추출 후 추가적인 코드를 통해 정제를 마친 텍스트들을 워드 클라우드로 시각화하여 표현


* * *


# 코드 수정 과정

1.각 카테고리별 링크를 url변수로 들고오고 그 안의 텍스트들을 한번더 크롤링할려했는데 다음뉴스는 하이퍼 링크가 /society"으로 표시되어 크롤링해도 제대로 된 url을 긁어올 수 없음
    
    <a href="/society" class="link_gnb" data-tiara-layer="society"><span class="txt_gnb">사회</span></a>

해결방법 - 여러 방법 중 미리 카테고리 링크를 주고 조건문을 사용하여 해결 
    
    category_links = {                                     #수정 후
        "사회": "https://news.daum.net/society#1",
        "경제": "https://news.daum.net/politics#1",
        "환경": "https://news.daum.net/economic#1",        #### 카테고리에 따른 뉴스 링크 설정
        "정치": "https://news.daum.net/foreign#1",
        "문화": "https://news.daum.net/culture#1",
        "IT": "https://news.daum.net/digital#1",
    }



2.top_noun_freq를 기반으로 워드 클라우드를 생성하는 과정에서 top_noun_freq 리스트 안에 튜플 형태로 단어와 빈도수가 저장되어 문자열로 입력받아야 하는 다음과 같은 코드에서 오류가 발생
          
          wc.generate_from_text(top_noun_freq)
         
         #오류 : expected string or bytes-like object

해결방법 - 앞에 str을 붙여줘 문자열로 변환 밑 replace를 통해 각 단어 양옆의 " "를 제거하여 워드 클라우드로 표현

          wc.generate_from_text(str(top_noun_freq).replace("'", ""))         #수정 후 


* * *
 
# 문제를 해결하며 

1. 미리 가져온 카테고리별 링크와 조건문을 통해 각각의 카테고리별 뉴스 내용들을 크롤링

2. 크롤링한 텍스트들을 토큰화, 불용어 처리, 명사 추출과 같이 전처리

3. 전처리한 단어들을 가지고 빈도수가 높은 중요한 단어들을 선별하고 워드 클라우드를 통한 시각화


* * *

# 코드 실행 결과
<img ![image](https://github.com/An-Jeong-Jin/Pretreatment-final/assets/120768669/791fd8e8-dd0d-488c-9cd0-c7b6ae4f2a7c)
>


* * *

# 코드 설명

코드내에 주석처리로 코드 설명

