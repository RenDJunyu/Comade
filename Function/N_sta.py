
import requests
import json
import re

#N station
url= "http://nexushd.org/signin.php?"
host='www.nexushd.org'
origin='http://www.nexushd.org'
referer='http://www.nexushd.org/signin.php'
cookie = "c_secure_uid=MTQxMzQ5; c_secure_pass=6af69e7fdf6a066a9610cc3d671a201a; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D"

header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':  'gzip, deflate',
    'Accept-Language':  'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':    'max-age=0',
    'Connection':       'keep-alive',
    'Content-Length':   '21',
    'Content-Type':     'application/x-www-form-urlencoded',
    'Cookie':   cookie,
    'Host':     host,
    'Origin':   origin,
    'Referer':  referer,
    "Upgrade-Insecure-Requests": "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}

checkin = requests.post(url,headers=header,data='action=post&content=3')
print(re.findall("已经.{10}",checkin.text))
# print(checkin.text)

cookie = "c_secure_uid=MTI3Njk3; c_secure_pass=e7e32f4e6c4d8b6d977b469dfcbc4524; c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D"
header['Cookie']=cookie
checkin = requests.post(url,headers=header,data='action=post&content=3')
print(re.findall("已经.{10}",checkin.text))
# print(checkin.text)

url= "https://www.jiepei.com/Member/Checkin?MbId=168147"
cookie= "CityId=2; 6F561D50DD3FA355=d437fec6f4f7e6456c6114237609fb6d; AdminId=52; IsFirstShowFlashAd=1; AGL_USER_ID=de37321a-81b9-4850-ae27-f42f0c9b7244; comeFrom=0; ASP.NET_SessionId=zrsdskwi11abrblr02u3efbq; PreambleUrl=https://cn.bing.com/; Qs_lvt_108071=1650275928%2C1651225842; Hm_lvt_415e74fa098b4c4bf3abf42b8d4d2a83=1650275928,1651225843; zmwfront=685910F925F5407EE4A415A02BA689A97C52D13FF74E7C11A9D5B23E6582570BBE1013887AAE5E75DA89B1816E6643CB94BD13FA697A0DD5A6F365DD946A32F7BA80AB547F19CDC199034C893FF20A6D849181A562E9EB42FD3D5912708DDF7B0635734FDCEE9F9E67E7BD8BF277A5EB96DF81DD6E4D9B6A823AB411321C1B260A0DB325; Hm_lpvt_415e74fa098b4c4bf3abf42b8d4d2a83=1651225854; Qs_pv_108071=505115244280606900%2C4163194212054121000%2C3827713242977957400%2C50376268391779864"
host= "www.jiepei.com"
origin= "https://www.jiepei.com"
referer= "https://www.jiepei.com/member/newmemberindex"

# sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# X-Requested-With: XMLHttpRequest

header={
    'Accept':'*/*',
    'Accept-Encoding':  'gzip, deflate, br',
    'Accept-Language':  'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':       'keep-alive',
    'Content-Length':   '0',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",

    'Cookie':   cookie,
    'Host':     host,
    'Origin':   origin,
    'Referer':  referer,
    "Upgrade-Insecure-Requests": "1",
}

checkin = requests.post(url,headers=header,data='MbId=168147')
print(checkin.json())
# print(checkin.text)