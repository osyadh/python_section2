import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20110630_83/kcy5510_1309418148748VUKrz_JPEG/%B1%E2%B4%CF%C7%C7%B1%D7.jpg"
htmlUrl = "http://google.com"

savePath1 = "/Users/seongdongho/Desktop/test1.jpg"
savePath2 = "/Users/seongdongho/Desktop/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print('download complete!')
