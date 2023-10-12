# 음성 처리

* * *
음성 파일 재생해보기

코드
    
    # 필요한 라이브러리 임포트
    import soundfile as sf
    import pydub
    # 음성 파일 경로 지정
    file_path = "Dancing Cartoon.wav"
    
    # 음성 파일 읽기
    data, sample_rate = sf.read(file_path)
    
    # 음성 파일의 메타 정보 출력
    print("Sample Rate:", sample_rate)
    print("Duration:", len(data) / sample_rate, "seconds")
    
    # # 음성 파일의 일부를 재생 #########실행이 안됨
    # audio = pydub.AudioSegment.from_file(file_path)
    # audio.play() 
    ###구글링  #### https://wikidocs.net/15214
    import pyglet
    song = pyglet.media.load("Dancing Cartoon.wav")
    song.play()
    # pyglet.app.run()

수정중!!!
