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
        RGB      ##빨강, 노랑, 파랑을 사용하는 컬러 이미지 

* * *
# 가로와 세로 길이가 표시된 이미지로 나타내기
  
  코드 

    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    
    img = Image.open('egg.png')
    img_np = np.array(img)   ## 이미지를 넘파이 배열로 반환
    plt.imshow(img_np)      ## matplotlib라이브러리를 통해 넘파이 배열로 저장된 이미지를 시각적으로 표현, 해당 픽셀 좌표축을 함께 표시
    plt.show()  #화면에 표시  

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



# 이미지 회전 

코드

    from PIL import Image
    img = Image.open('egg.png')
    
    img_rotated = img.rotate(180)  ### 회전 각도
    
    img_rotated.show()

실행결과
<img width="638" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/c7a166d4-76b8-4faf-a2e4-7777bc788418">


# 이미지 좌우대칭,상하대칭

코드 
    
    from PIL import Image
    img = Image.open('egg.png')
    
    img_flipped_LR = img.transpose(Image.FLIP_LEFT_RIGHT) ### FLIP_LEFT_RIGHT = 좌우대칭 
    img_flipped_LR.show()
    
    img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM) ### FLIP_TOP_BOTTOM = 상하대칭
    img_flipped_TB.show()

실행결과
<img width="639" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/cbb9b38b-cfd8-41d9-a6db-4a7cc5310f72">
<img width="640" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/1ea6c818-89a4-4e6e-99e2-d43a63376c49">


# 이미지 배경 없애기 
코드(코랩)

    from rembg import remove  ## 컬러 기반, 색상으로 배경과 객체를 구분
    from PIL import Image
    from google.colab import drive
    drive.mount('/content/drive')
    input = Image.open('/content/drive/MyDrive/Colab Notebook/img/egg.png') # load image
    output = remove(input) # 배경 삭제
    output.save('/content/drive/MyDrive/Colab Notebook/img/regg.png') # save image

실행결과

<img width="657" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/756a654e-c5f6-4af5-a9b8-057d8023b67e">

# 이미지 합병

코드

    from PIL import Image
    img_01 = Image.open("cloud.jpg")  ### 배경으로 쓸 이미지 
    img_02 = Image.open("rm_egg.png")  ### 붙일 이미지 
    img_01_size = img_01.size   ## 이미지의 크기를 얻어 변수에 저장
    new_im = Image.new('RGB', img_01_size, (250, 250, 250))   ## 새로운 이미지 생성, img_01과 사이즈 동일시 하기 위해 img_01_size삽입 #(250, 250, 250)는 크게 의미X 새로운 이미지 색을 회색으로 만듬
    new_im.paste(img_01, (0, 0)) ### 회색으로 된 new_im위에 img_01을 덮음 
    new_im.paste(img_02, (40, 10), img_02)  img_01 이미지 위에 img2이미지를 40, 10위치에 붙임
    new_im.show()
    print(new_im.format, new_im.size, new_im.mode)


img_01 = <img width="1021" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/ece24457-3b53-4eee-940f-6db91912064d">


img_02 = <img width="739" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/37279599-b150-485a-9898-a1ef286a3e77">

실행결과

<img width="373" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/27ae5e16-7bfa-432d-b5dc-63dfc1a71289">



  
# 이미지 필터링 

코드

    from PIL import Image
    img = Image.open('egg.png')
    img_gray = img.convert("L")
    img_gray.show() ##흑백 이미지 
    
    from PIL import ImageFilter
    
    img_blur = img.filter(ImageFilter.GaussianBlur(10))###Blur 효과를 줄 때 가장 많이 사용하는 가우시안 블러로 숫자를 크게 할수록 흐려짐
    img_blur.show()  ## 흐린 이미지
    
    from PIL import Image
    img = Image.open('egg.png')
    img_edge = img.filter(ImageFilter.EDGE_ENHANCE)
    img_edge.show()   ## 엣지 강조 이미지 
    print(img_edge.format, img_edge.size, img_edge.mode)

실행결과
![image](https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/031c53df-11fe-4aac-9fe9-3dbc63d1793d)

![image](https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/2fa01af5-c628-4002-895f-3356f1952f8f)

![image](https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/bfda5e79-7d84-4947-a8ce-369569261c02)

# 이미지 바이트 배열로 변환

코드

    from PIL import Image
    import io     ## 메모리에서 입출력을 위해 사용 
    img = Image.open("egg.png")
    img_byte = io.BytesIO()    ## 이미지 데이터를 담을 객체 생성
    img.save(img_byte, format="PNG")    객체에 PNG형식으로 저장
    img_byte1 = img_byte.getvalue()  getvalue()를 통해 저장된 이미지를 바이트로 가져옴
    print(img_byte1[:2])  

실행결과
  
    b'\x89P'
# 이미지 넘파이 배열로 변환

코드

    ##이미지 넘파이배열로 바꾸고 넘파이 배열을 이미지로 바꾸기 
    import numpy as np
    from PIL import Image
    
    img = Image.open('egg.png')
    img.show()
    
    x = np.array(img) ## 이미지 -> 넘파이 배열
    print(x)
    
    img = Image.fromarray(x) ## 넘파이 배열 -> 이미지 
    img.show()

실행결과

  <img width="373" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/12f0d66e-2bfc-4a43-8a16-5ad760e628e7">
    
    
    
    [[[238 215 184]
      [238 215 184]
      [238 215 184]
      ... 생략
    
  <img width="373" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/cea1ca85-3ff4-43fb-b138-684d21b0ab86">

  
