from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
# import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/all-courses/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

top = soup.select("ul#course-list .item-title")

for i,rec in enumerate(top,1) :
    print(i,rec.select_one("a").string)
