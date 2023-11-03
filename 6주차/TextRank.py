import requests
from bs4 import BeautifulSoup
from gensim.summarization import keywords, summarize
import re

num_pages = 3
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

combine_list = []

for page_num in range(1, num_pages + 1):
    a = []
    url = f'https://www.82cook.com/entiz/enti.php?bn=10&page={page_num}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    t = soup.select('#bbs > ul > li > div > a')

    for i in t:
        a.append(i.get('href'))

    for text in a:
        link = "https://www.82cook.com/entiz/" + text
        res = requests.get(link, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')

        content = soup.select('#column2')
        for i in content:
            title = i.select_one('#readTitle > h2').text.strip()
            text = i.select_one('#articleBody').text.strip()

            recipe_keywords = keywords(text, words=5, split=True, scores=True, lemmatize=True)    ### TextRank 알고리즘을 사용하여 레시피 추출적 요약
            recipe_summarize = summarize(text, word_count=50)

            
            summarize_recipe = f"레시피: {title}\n키워드: {recipe_keywords}\n요약된 레시피: {recipe_summarize}"  ### 레시피 제목과 내용을 결합하여 저장
            combine_list.append(summarize_recipe)


for index, summary in enumerate(combine_list):    ### 요약된 레시피 출력
    print(f"Recipe {index + 1} 요약:\n{summary}\n")
