from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt
nltk.download('punkt')
nltk.download('stopwords')

                               # 웹 페이지에서 뉴스 기사 스크랩


url = "https://news.daum.net/society#1"                       # 웹 페이지 URL 설정
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')           # 웹 페이지 요청 및 HTML 파싱


a = []


newslist = soup.select(".list_newsmajor li")


for news_item in newslist:
    link_txt = news_item.select_one(".link_txt")['href']
    article_res = requests.get(link_txt, headers=headers)
    article_soup = BeautifulSoup(article_res.text, 'lxml')
    
    
    news_content = article_soup.select_one(".article_view").text.replace("\n", "")
    
    
    a.append(news_content)

                                                   # 텍스트 전처리 및 토큰화

# aa = []
# for string in a:
#     aa.append(string.strip())

# aaa = []
# for string in aa:
#     aaa.append(string.replace(".", ""))

aa = [string.strip() for string in a]
aaa = [string.replace(".", "") for string in aa]
# aaaa = str(aaa)


t_text = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', aaaa)     # 특수 문자 괄호 제거하여 정제된 텍스트 생성


token = word_tokenize(t_text)        # 텍스트를 단어로 토큰화

 
k_stopwords = set(['은', '는', '이', '가', '에', '에게', '로', '입니다', '것' ])        # 한글 불용어 목록 
 



f_tokens = []
for word in token:                # 불용어 제거
    if word not in k_stopwords:
        f_tokens.append(word)

f_words = []
for word in f_tokens:          
    if not re.search(r'[a-zA-Z0-9]', word):         # 영어나 숫자가 포함된 단어 제거
        f_words.append(word)




okt = Okt()
nouns = okt.nouns(str(f_words))          # Okt 형태소 분석기를 사용하여 명사 추출




word_freq = Counter(nouns)       # 명사의 빈도를 계산

print(word_freq)
