import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# imgUrl = "https://nv.veta.naver.com/fxclick?eu=EU10000120&calp=-&oj=bbC87fref33KPV%2FCG3pMA%2FJf87%2BNaUSAzWiXZhRHK77f64LySk5xV8IROQ19196lak8U1Qq8SSAykAoyPN7M7%2BGudwCHPJEkC%2FkFcnTSG15syEy1CZskIQ&ac=7775979&src=3676506&br=2815857&evtcd=P901&x_ti=837&tb=&oid=&sid1=&sid2=&rk=9783c5ada73504fccc2aa6276593bea8&eltts=AXP7jIlo3dNpBizCTXcSiQ%3D%3D&lu=&brs=Y&"
movieUrl = "http://streaming.parkcoach.com/basic/201405/01/backas_basic_news1.mp4"

# savePath1 = "/Users/seongdongho/Desktop/mework_img.jpg"
savePath2 = "/Users/seongdongho/Desktop/homework_movie.mp4"

# dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(movieUrl, savePath2)

print('download complete!')
