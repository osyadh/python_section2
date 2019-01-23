from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
<div id="main">
    <h1>Lecture</h1>
    <ul class="lecs">
        <li>python basic programing</li>
        <li>machine learning</li>
        <li>android bluetooth programing</li>
    </ul>
</div>
</html></body>
"""

soup = BeautifulSoup(html, "html.parser")
h1 = soup.select_one("div#main > h1")
print(h1.string)

# for z in h1 :
#     print(z.string)
# 귀찮으니 select <list> -> select_one <class 'bs4.element.Tag'>

li = soup.select("div#main > ul.lecs > li")
for li in li :
    print(li.string)
