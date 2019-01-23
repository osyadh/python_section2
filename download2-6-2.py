from bs4 import BeautifulSoup
import sys
import io
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open(os.path.expanduser("~/Desktop/inflern/section2/food-list.html"), encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ac-list > li:nth-of-type(4)").string)
print(soup.select("#ac-list > li[data-lo='cn']")[0].string)
print(soup.select("#ac-list > li.alcohol.high")[0].string)
# class 띄워쓰기 있을때 .으로 연결 id인 경우는 #

param = {"data-lo" : "cn", "class" : "alcohol high"}
print(soup.find("li", param).string)
# print(soup.find(id="ac-list").find("li", param).string)

for ac in soup.find_all("li"):
    if ac["data-lo"] == "us" :
        print(ac.string)
