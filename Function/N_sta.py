
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
print(re.findall("你已经.{10}",checkin.text))
print(checkin.text)