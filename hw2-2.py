import io
import sys
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://nv.veta.naver.com/fxclick"

value1 = {
'eu' : 'EU10000119'
}

value2 = {
'calp' : '-'
}

value3 = {
'oj' : 'bbC87fref337WxFM4CXK9fJf87%2BNaUSAzWiXZhRHK77f64LySk5xV8IROQ19196lak8U1Qq8SSAykAoyPN7M7%2BGudwCHPJEkC%2FkFcnTSG15syEy1CZskIQ'
}

value4 = {
'ac' : '7774409'
}

value5 = {
'src' : '3680092'
}

value6 = {
'br' : '2817609'
}

value7 = {
'evtcd' : 'P901'
}

value8 = {
'x_ti' : '941'
}

value9 = {
'rk' : '97b60ee111ad4d83ebdf7d7a0430c40c'
}

value10 = {
'eltts' : 'AXP7jIlo3dNpBizCTXcSiQ%3D%3D'
}

value11 = {
'brs' : 'Y'
}

param1 = urlencode(value1)
param2 = urlencode(value2)
param3 = urlencode(value3)
param4 = urlencode(value4)
param5 = urlencode(value5)
param6 = urlencode(value6)
param7 = urlencode(value7)
param8 = urlencode(value8)
param9 = urlencode(value9)
param10 = urlencode(value10)
param11 = urlencode(value11)

url = API+"?"+param1+'&'+param2+'&'+param3+'&'+param4+'&'+param5+'&'+param6+'&'+param7+'&'+param8+'&'+param9+'&'+param10+'&'+param11
# print(url)

reqData = req.urlopen(url).read()
# print(reqData)

savePath = "/Users/seongdongho/Desktop/movie.mp4"

with open(savePath,'wb') as saveFile:
    saveFile.write(reqData)

print("Finished!")
