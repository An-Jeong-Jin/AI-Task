# 이미지 처리 
* * *
# 이미지 불러오기 및 정보확인
  코드
  
    from PIL import Image
    img = Image.open('egg.png')  ##사진은 https://pixabay.com/ko/에서 가져옴
    img.show()
    print(img.filename)  ##이미지 이름
    
    print(img.format) ### 이미지 형식
    
    print(img.size)#### 이미지 크기
    
    print(img.width) #### 이미지 너비
           
    print(img.height)  ##이미지 높이
    
    print(img.mode)  ## 이미지 색 모드

실행결과
    
  <img width="525" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/efe493d4-dcff-4083-ac72-88c6b77acd19">
        
        egg.png
        JPEG
        (1280, 905)
        1280
        905
        RGB

* * *
# 가로와 세로 길이가 표시된 이미지로 나타내기
  
  코드 

    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    
    img = Image.open('egg.png')
    img_np = np.array(img)
    plt.imshow(img_np)
    plt.show()

  실행결과

  <img width="586" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/423a4063-287b-4eae-a730-1c8d9dca0bf4">



# 이미지 사이즈 변경

코드 

    from PIL import Image
    
    img = Image.open('egg.png')
    img_resized = img.resize((300, 400))
    
    
    img_resized.show()  ### 변경한 사이즈 
    
    img.show()  #### 원본 사이즈     

  실행결과

<img width="145" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/525950c7-a109-44e8-bf30-311209d00ac3">

<img width="638" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/c70fa292-b596-4d43-ba84-26e589b17514">

# 이미지 자르기
코드
  
    from PIL import Image
    img = Image.open('egg.png')
    
    img_cropped = img.crop((200, 150,1000, 1000))  ###좌표로 그림을 자른다고 이해하자, ##crop(가로시작점, 세로시작점, 가로범위, 세로범위)
                                             
    img_cropped.show() #### 잘라낸 이미지
실행결과

<img width="397" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/3860e13c-ccce-4b0c-9103-7b9c7d377112">











  
