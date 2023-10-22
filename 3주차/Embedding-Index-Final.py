import requests
from bs4 import BeautifulSoup
import re
from google.colab import drive

num_pages = 3

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

combine_list = []

for page_num in range(1, num_pages + 1):       ##레시피를 긁어올 범위설정, 웹 구조가 해당페이지의 숫자가 뒤에 붙음
  a = []
  url = f'https://www.82cook.com/entiz/enti.php?bn=10&page={page_num}'  
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, 'lxml')
  t = soup.select('#bbs > ul > li > div > a')            ### 각 레시피로 들어가는 링크 긁기
  for i in t:
    a.append(i.get('href'))

  for text in a:
    link = "https://www.82cook.com/entiz/" + text        #####다른 사이트와 다르게 href="read.php?bn=10&num=3245201&page=0"와 같이 뒷부분만 가져올 수 있어 해당 링크에 붙여줌
    res = requests.get(link, headers=headers)              ##### n개의 레시피의 하이퍼링크로 들어가기
    soup = BeautifulSoup(res.text, 'lxml')

    content = soup.select('#column2')                  ### n번째 레시피에서 for문을 통해 제목, 텍스트 요소를 찾아 title, text변수로 바로 할당
    for i in content:
      title = i.select_one('#readTitle > h2').text.strip().replace(" ", "").replace("※", "").replace("!", "")      ######전체를 포함하는 박스에서 레시피 이름만 가져오기
      text = i.select_one('#articleBody').text.strip().replace(" ", "").replace("※", "").replace("!", "")          ######전체를 포함하는 박스에서 레시피 내용만 가져오기
      text = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ ]', '', text)          ##### 한글을 제외한 모든 문자 제거
      title = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ ]', '', title)        ##### 한글을 제외한 모든 문자 제거
      combine_text = f"메뉴: {title}\n레시피: {text}"            ## 제목이랑 내용 합치기
      combine_list.append(combine_text)                        ### 리스트에 저장

#####크롤링한 레시피들 출력
for i in combine_list:
  print(f"Hit recipe \n {i}\n")                            
#####드라이브 마운트
drive.mount('/content/drive')
##### 해당경로로 저장
for idx, combine_text in enumerate(combine_list):                  #idx 와  enumerate함수를 통해 현재 요소의 인덱스 추적 및 표시 즉 enumerate함수가 순서를 매겨서 idx에 할당시킴
    file_name = f'/content/drive/MyDrive/Colab Notebook/recipe/레시피_{idx + 1}.txt'          
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(combine_text)
##################### 크롤링 후 전처리 및 드라이브 마운트를 통한 레시피 텍스트 파일저장 
#######################임베딩 및 색인 시작
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

from langchain.embeddings import LlamaCppEmbeddings, HuggingFaceEmbeddings
######


embeddings = HuggingFaceEmbeddings()
######

from google.colab import drive
drive.mount('/content/drive')
######

fn_dir = "/content/drive/My Drive/Colab Notebook/recipe"
######

loader = DirectoryLoader(fn_dir)          ##### 객체 생성및 해당 디렉토리에 텍스트 문서 로드
documents = loader.load()### 텍스트문서 로드 및 documents에 저장

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0) # 텍스트들을 1000단위로 분활 중복 청크 X
docs = text_splitter.split_documents(documents)## 데이터 분활 및 docs에 저장

len(documents), len(docs)
######

db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="recipe_index_hf")      ### 크로마 객체를 생성하여 텍스트 데이터 특성 추출 및 임베딩 persist_directory="recipe_index_hf"는 인덱스를 저장할 공간
db.persist()  #지정된 위치에 저장
######

query = "전남친 토스트 레시피 알려줘"
docs = db.similarity_search(query)  #### 가장 근처의 문서들에 접근 및 반환
######

docs[:5]



