from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
# import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/?nil_top=mobile"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

top = soup.find_all(tabindex="-1")

# print(top)

for i,e in enumerate(top,1) :
    print(i,e.string)
