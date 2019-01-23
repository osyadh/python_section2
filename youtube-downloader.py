import pytube
import os
import subprocess

# 다운 받을 동영상 URL 지정
yt = pytube.YouTube(input("유튜브 주소를 입력하세요"))
# 유튜브 url을 입력하세요
videos = yt.streams.all()

# print("videos",videos)

for i in range(len(videos)):
    print(i, videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "/Users/seongdongho/documents/youtube/"

videos[cNum].download(down_dir)

choise = input("mp3로 변환 하시겠습니까? y/n :")
if choise == 'y':
    newFileName = input("변환 할 mp3 파일명은?")
    oriFileName = videos[cNum].default_filename

    subprocess.call(['ffmpeg','-i',
        os.path.join(down_dir,oriFileName),
        os.path.join(down_dir,newFileName)
    ])
    print("동영상 다운로드 및 mp3 변환 완료!")
elif choise == 'n':
    print("끝!")
else :
    print("y나 n을 입력해주세요")

# ffmpeg 설치 안되서 mp3변환 안됨!
