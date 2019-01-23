from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
# import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://m.finance.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

# print(soup.prettify)

top = soup.select("table#myRecentListTemp tr")

# print(type(top))

for i,e in enumerate(top,1) :
    print(i,e.find("th",{"class" : "name"}).string,e.find("td",{"class": "idx"}).string)

for i,e in enumerate(top,1) :
    print(i,e.select_one(".name").string,e.select_one(".idx").string)
