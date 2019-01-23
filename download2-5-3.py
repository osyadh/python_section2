from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
 <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.google.com">google</a></li>
    <li><a href="http://www.tistory.com">tistory</a></li>
 </ul>
</html></body>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print(type(links))
# a = soup.find_all("a", string="daum")
# a = soup.find_all("a", limit=3)
# a = soup.find_all(string=["naver","daum"])
# print(a)

for a in links:
    # print(type(a),a)
    href = a.attrs["href"]
    txt = a.string
    print("txt >>",txt,"\nhref >>", href)
