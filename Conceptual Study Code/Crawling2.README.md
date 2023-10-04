# crawling2
crawling.Musins.Denim Pants(과제용)


# 1.주제 
주제 - 인기 순위별 청바지 제품 이름, 가격, 이미지, 링크등의 정보 공유
* * *

## 2.문제 및 해결방안

# 코드1

    image_link = item.select_one(".list_img")

# 출력값1

    제품: 이지 와이드 데님 팬츠 그레이
    할인가격: 52,800원
                  42,000원
    이미지: <div class="list_img">
    <a class="img-block" href="//www.musinsa.com/app/goods/2092852" name="goods_link" title="이지 와이드 데님 팬츠 그레이">
    <img alt="굿라이프웍스(GLW) 이지 와이드 데님 팬츠 그레이" class="lazyload lazy" data-original="https://image.msscdn.net/images/goods_img/20210826/2092852/2092852_16907882732904_125.jpg" 
    src="//image.msscdn.net/images/no_image_125.png"/>
    </a>
    </div>
    링크: //www.musinsa.com/app/goods/2092852
 
 
 코드 1로 실행하면 위와 같이 html부분이 출력
 list_img 클래스의 <img>을 선택하고 data-original' 를 이용하여 해당 이미지의 실제 경로를 가져옴

* * *


# 코드2
    
        price = item.select_one(".price").text.strip()   

# 출력값2

    제품: 이지 와이드 데님 팬츠 그레이
    할인가격: 52,800원
                42,000원
    이미지: https://image.msscdn.net/images/goods_img/20210826/2092852/2092852_16907882732904_125.jpg
    링크: //www.musinsa.com/app/goods/2092852

 
 원가, 할인된 가격 2개가 동시에 뜨는 경우가 있어 출력값2 처럼 할인 가격이 2개로 출력
 원가와 할인된 가격은 띄어쓰기 되있는 점을 이용해 split()과 인덱스를 활용하여 할인된 가격만 표시

  
   


# 3.아쉬움 점 및 응용할 점 

옷들의 정보를 가져오는 위의 코드를 통해 청바지 뿐이 아닌 인기 제품의 여러 옷들을 인기 순위별로 크롤링하는 코드 제작 중
