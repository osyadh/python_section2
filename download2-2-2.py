import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20110630_83/kcy5510_1309418148748VUKrz_JPEG/%B1%E2%B4%CF%C7%C7%B1%D7.jpg"
htmlUrl = "http://google.com"

savePath1 = "/Users/seongdongho/Desktop/test1.jpg"
savePath2 = "/Users/seongdongho/Desktop/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1,'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)
# with 문은 벗어나면 자동 close되기 때문에 close 필요없음, 더 추천!

print('download complete!')

# urlretrieve는 바로 저장, urlopen은 메모리 저장 후 조작 후 저장가능
