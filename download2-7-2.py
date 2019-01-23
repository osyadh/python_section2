from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
# import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('euc-kr')
soup = BeautifulSoup(res,"html.parser")

# print(soup.prettify)

top = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top :
    if e.find("a") is not None :
        print(i, e.select_one(".tltle").string)
        i += 1
