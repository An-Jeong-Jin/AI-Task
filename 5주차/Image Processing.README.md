# 이미지 처리 
* * *
# 이미지 불러오기 및 정보확인
  코드
  
    from PIL import Image
    img = Image.open('egg.png')
    img.show()
    print(img.filename)  ##이미지 이름
    
    print(img.format) ### 이미지 형식
    
    print(img.size)#### 이미지 크기
    
    print(img.width) #### 이미지 너비
           
    print(img.height)  ##이미지 높이
    
    print(img.mode)  ## 이미지 색 모드

실행결과
    
        egg.png
        JPEG
        (1280, 905)
        1280
        905
        RGB
