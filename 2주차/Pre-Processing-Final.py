#pip install konlpy

#from google.colab import drive
#drive.mount('/content/drive')

import requests
from bs4 import BeautifulSoup
import re  ## 정규 표현을 사용하여 텍스트에서 패턴 검색 및 추출하는데 사용용
import nltk
from nltk.tokenize import word_tokenize  
from konlpy.tag import Okt
from collections import Counter      #### 갯수 세는데 사용
import matplotlib.pyplot as plt        
from wordcloud import WordCloud
from collections import Counter
nltk.download('punkt')   ###### 자연어처리를 위한 필요한 데이터 자원을 다운으로 하는데 사용
nltk.download('stopwords')

                                                                        #### 불용어 목록 정의
korean_stopwords = set([ '가', '가까스로', '가령', '각', '각각', '각자', '각종', '갖고말하자면', '같다', '같이', '개의치않고',
    '거니와', '거바', '거의', '것', '것과 같이', '것들', '게다가', '게우다', '겨우', '견지에서', '결과에 이르다',
    '결국', '결론을 낼 수 있다', '겸사겸사', '고려하면', '고로', '곧', '공동으로', '과', '과연', '관계가 있다',
    '관계없이', '관련이 있다', '관하여', '관한', '관해서는', '구', '구체적으로', '구토하다', '그', '그들',
    '그때', '그래', '그래도', '그래서', '그러나', '그러니', '그러니까', '그러면', '그러므로', '그러한즉',
    '그런 까닭에', '그런데', '그런즉', '그럼', '그럼에도 불구하고', '그렇게 함으로써', '그렇지', '그렇지 않다면',
    '그렇지 않으면', '그렇지만', '그렇지않으면', '그리고', '그리하여', '그만이다', '그에 따르는', '그위에',
    '그저', '그중에서', '그치지 않다', '근거로', '근거하여', '기대여', '기점으로', '기준으로', '기타', '까닭으로',
    '까악', '까지', '까지 미치다', '까지도', '꽈당', '끙끙', '끼익', '나', '나머지는', '남들', '남짓', '너',
    '너희', '너희들', '네', '넷', '년', '논하지 않다', '놀라다', '누가 알겠는가', '누구', '다른', '다른 방면으로',
    '다만', '다섯', '다소', '다수', '다시 말하자면', '다시말하면', '다음', '다음에', '다음으로', '단지', '답다',
    '당신', '당장', '대로 하다', '대하면', '대하여', '대해 말하자면', '대해서', '댕그', '더구나', '더군다나',
    '더라도', '더불어', '더욱더', '더욱이는', '도달하다', '도착하다', '동시에', '동안', '된바에야', '된이상',
    '두번째로', '둘', '둥둥', '뒤따라', '뒤이어', '든간에', '들', '등', '등등', '딩동', '따라', '따라서',
    '따위', '따지지 않다', '딱', '때', '때가 되어', '때문에', '또', '또한', '뚝뚝', '라 해도', '령', '로',
    '로 인하여', '로부터', '로써', '륙', '를', '마음대로', '마저', '마저도', '마치', '막론하고', '만 못하다',
    '만약', '만약에', '만은 아니다', '만이 아니다', '만일', '만큼', '말하자면', '말할것도 없고', '매', '매번',
    '메쓰겁다', '몇', '모', '모두', '무렵', '무릎쓰고', '무슨', '무엇', '무엇때문에', '물론', '및', '바꾸어말하면',
    '바꾸어말하자면', '바꾸어서 말하면', '바꾸어서 한다면', '바꿔 말하면', '바로', '바와같이', '밖에 안된다',
    '반대로', '반대로 말하자면', '반드시', '버금', '보는데서', '보다더', '보드득', '본대로', '봐', '봐라', '부류의 사람들',
    '부터', '불구하고', '불문하고', '붕붕', '비걱거리다', '비교적', '비길수 없다', '비로소', '비록', '비슷하다',
    '비추어 보아', '비하면', '뿐만 아니라', '뿐만아니라', '뿐이다', '삐걱', '삐걱거리다', '사', '삼', '상대적으로 말하자면',
    '생각한대로', '설령', '설마', '설사', '셋', '소생', '소인', '솨', '쉿', '습니까', '것'])


category = input("뉴스 카테고리를 입력하세요 (사회, 경제, 환경, 정치, 문화, IT): ")      #### 카테고리 선택


category_links = {
    "사회": "https://news.daum.net/society#1",
    "경제": "https://news.daum.net/politics#1",
    "환경": "https://news.daum.net/economic#1",        #### 카테고리에 따른 뉴스 링크 설정
    "정치": "https://news.daum.net/foreign#1",
    "문화": "https://news.daum.net/culture#1",
    "IT": "https://news.daum.net/digital#1",}


if category not in category_links:
    print("해당 카테고리는 존재하지 않습니다")
else:
    url = category_links[category]                ### url을 딕셔너리 value값을 통해 불러옴
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
   soup = BeautifulSoup(res.text, 'lxml')                  
    news_content_list = []
    newslist = soup.select(".list_newsmajor li")            #### li, li, li, li를 포함한 박스

    for news_item in newslist:
        link_txt = news_item.select_one(".link_txt")['href']      ## n개의 li의 링크를 담고  그 링크를 타고 들어가 텍스트 부분을 지정하는 요소에서 텍스트만을 추출하여 리스트에 저장
        article_res = requests.get(link_txt, headers=headers)            
        article_soup = BeautifulSoup(article_res.text, 'lxml')
        news_content = article_soup.select_one(".article_view").text.replace("\n", "")
        news_content_list.append(news_content)



    cleaned_text = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', str(news_content_list))           #### 특수 문자와 괄호 제거


    tokens = word_tokenize(cleaned_text)           ######## 토큰화


    filtered_tokens = [word for word in tokens if word not in korean_stopwords]               ##### 불용어 처리 & 영어, 숫자 제거 & 1글자 단어 제거
    filtered_words = [word for word in filtered_tokens if not re.search(r'[a-zA-Z0-9]', word)]
    Word_tokens = [word for word in filtered_words if len(word) > 1]

    okt = Okt()                                                        ##### 명사 추출
    nouns = okt.nouns(str(Word_tokens))
    nouns = [word for word in nouns if len(word) > 1]
    noun_freq = Counter(nouns)                                        ####문자 빈도수

    top_noun_freq = noun_freq.most_common(500)               #### 단어의 빈도수가 높은 것 순으로 재배열

    print(top_noun_freq)

                                                                 #### 워드 클라우드 생성

    wc = WordCloud(
        max_words=50,      ## 최대 단어수
        random_state=810,   ## 난수 / 동일해야 코드 돌려도 같은 값 출력
        background_color='white',
        font_path='/content/drive/MyDrive/JJJ.File/NanumSquareRoundEB.ttf')  ## 글꼴
    wc.generate_from_text(str(top_noun_freq).replace("'", ""))    ## 워드 클라우드 생성, ' ' 을 없애줌

                                                                ### 워드 클라우드 시각화
    plt.figure(figsize=(8, 8)) 크기
    plt.imshow(wc)      # 워드클라우드 이미지 표시      
    plt.axis('off')  # 그래프  
    plt.show()  # 화면에 출력력

  
