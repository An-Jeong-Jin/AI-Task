########3주차 크롤링 코드 완성

import requests
from bs4 import BeautifulSoup
import re
from google.colab import drive
url = 'https://www.82cook.com/entiz/enti.php?bn=10'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
a = []
link_list = []

t = soup.select('#bbs > ul > li > div > a')
for i in t:
    a.append(i.get('href'))

for text in a:
    link = "https://www.82cook.com/entiz/" + text
    link_list.append(link)
l = []
t = []
for link in link_list:
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    content = soup.select('#column2')
    for i in content:
        l.append(i.select_one('#readTitle > h2').text.strip().replace(" ", "").replace("※", "").replace("!", ""))    ###전처리도 동시에
        t.append(i.select_one('#articleBody').text.strip().replace(" ", "").replace("※", "").replace("!", ""))
combine_list = []
for text, title in zip(t, l):
    title = ''.join(title.split()) ####들여쓰기 공백 지우기
    text = ''.join(text.split())
    combine_text = f"메뉴: {title} \n 레시피:{text}"
    combine_list.append(combine_text)
print(combine_list[3])

####드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')
#### 해당경로로 저장
for index, combine_text in enumerate(combine_list):
    file_name = f'/content/drive/MyDrive/Colab Notebook/recipe/레시피_{index+1}.txt'
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

loader = DirectoryLoader(fn_dir)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

len(documents), len(docs)
######

db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="recipe_index_hf")
db.persist()
######

query = "토스트"
docs = db.similarity_search(query)
######

docs[:5]



