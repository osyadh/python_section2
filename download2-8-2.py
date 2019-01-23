from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

url = "https://www.inflearn.com/all-courses/"

res = req.urlopen(url)
savePath = "/Users/seongdongho/Desktop/imagedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("#course-list > li")

for i, e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("div.item-title > a").string)
    fullFileName = os.path.join(savePath, str(i)+'.png') #jpg
    req.urlretrieve(e.select_one("div.item-avatar > a > img")['src'],fullFileName)

print("다운로드 완료 하하하")
