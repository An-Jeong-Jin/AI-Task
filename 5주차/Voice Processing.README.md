# 음성 처리

* * *
# 음성 파일 메타정보 출력 및 재생

코드
    
    # 필요한 라이브러리 임포트
    import soundfile as sf
    # 음성 파일 경로 지정
    file_path = "Voice.wav"
    
    # 음성 파일 읽기
    data, sample_rate = sf.read(file_path) ###soundfile 라이브러리를 통해 데이터, 샘플 레이트(우리가 듣는 소리를 숫자화) 불러옴
    
    # 음성 파일의 메타 정보 출력
    print("Sample Rate:", sample_rate)
    print("Duration:", len(data) / sample_rate, "seconds")
    
    # # 음성 파일의 일부를 재생 #########실행이 안됨
    # audio = pydub.AudioSegment.from_file(file_path)
    # audio.play() 
    ###구글링  #### https://wikidocs.net/15214
    import pyglet
    song = pyglet.media.load("Voice.wav")
    song.play()
    # pyglet.app.run()

실행결과
    
    Sample Rate: 44100
    Duration: 195.1608163265306 seconds
    음악실행
# 음성파일 변환

코드

    from pydub import AudioSegment   ### pydub 라이브러리를 통한 샘플 레이트 조정  ### 오류로 인해 코랩에서 실행
    filepath = '/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav'    
    audio = AudioSegment.from_file(filepath)
    new_sample_rate = 22000                ##샘플 레이트를 44000에서 22000으로 변경
    audio = audio.set_frame_rate(new_sample_rate)
    
    output_path = '/content/drive/MyDrive/Colab Notebook/audio/22hzVOICE.wav'
    audio.export(output_path, format="wav")
# 음성파형 (wav) 그려보기
코드

    import librosa
    import matplotlib.pyplot as plt
    import librosa.display
    y, sr = librosa.load('/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav') # y = 오디오 데이터, sr = 샘플 레이트
    plt.figure(figsize =(16,6))        # 가로 16, 높이 6인 그림 생성성
    librosa.display.waveshow(y =y, sr = sr)  # 오디오 데이터 시각화
    plt.show()

실행결과

<img width="1066" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/b1d980a6-7435-4791-b4f3-09330875edde">

# 음성파일을 푸리에변환 

푸리에변환 = (시간 영역 데이터를 주파수 영역으로 변경) = {시계열 데이터를 작은 시간 슬라이드창(윈도우)로 나누고 각 슬라이딩 창에서 FFT를 수행하여 주파수 정보 계산}

코드
    
    import numpy as np
    import librosa
    
    y , sr = librosa.load('/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav') 
    D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))     ###n_fft = FFT연산에 사용되는 윈도우 크기 지정/ 주파수 해상도와 비례    hop_length = 슬라이드창을 512 샘플링 포인트 마다 이동시킴   / 절댓값 / 넘파이

    print(D.shape)            ## 배열의 차원정보확인 및 행 크기 , 열크기 출

    plt.figure(figsize=(16,6))
    plt.plot(D) 
    plt.show()
실행결과

 <img width="1144" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/8cfe58b5-f8e7-4389-90b8-88c12e33a338">

# 음성파일  스펙트로그램 시각화
코드

    import librosa
    y , sr = librosa.load('/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav') 
    DB = librosa.amplitude_to_db(D, ref=np.max) #amplitude(진폭) -> DB(데시벨)로 바꿔라 ## ref=np.max는 데시벨로 변환할때 참조되는 값/ 주로 스펙트럼의 최댓값을 사용

    plt.figure(figsize=(16,6))
    librosa.display.specshow(DB,sr=sr, hop_length=512, x_axis='time', y_axis='log')#hop_length = 해상도 결정 및 스펙트로그램의 각 열 간의 간격
    plt.colorbar()  # 색입히기

실행결과

<img width="1121" alt="image" src="https://github.com/An-Jeong-Jin/AI-Task/assets/120768669/87cefbe7-2a30-47bc-93f9-2374fe2c3664">

# 음성파일 자르기
코드
    
    from pydub import AudioSegment
    filepath = ('/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav')
    audio = AudioSegment.from_file(filepath)
    start = 50000
    end = 55000                ###50초~55초 
    cut_audio = audio[start:end]
    outputfile = ("/content/drive/MyDrive/Colab Notebook/audio/VOICE.wav")
    cut_audio.export(outputfile, format="wav")
# 아쉬운 점
경로 지정 오류
모듈 다운로드 오류
