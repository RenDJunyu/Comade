
import requests
import json
import re

#N station
host='v6.nexushd.org'
origin='https://v6.nexushd.org'
referer='https://v6.nexushd.org/signin.php'
url= "https://v6.nexushd.org/signin.php?"
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
cookie = "c_secure_uid=MTQxMzQ5; c_secure_pass=6af69e7fdf6a066a9610cc3d671a201a; c_secure_ssl=bm9wZQ==; c_secure_tracker_ssl=bm9wZQ==; c_secure_login=bm9wZQ=="

header={
    'accept-encoding':  'gzip, deflate',
    'accept-language':  'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control':    'max-age=0',
    'connection':       'keep-alive',
    'content-length':   '21',
    'content-type':     'application/x-www-form-urlencoded',
    'cookie':   cookie,
    'host':     host,
    'origin':   origin,
    'referer':  referer,
    "Upgrade-Insecure-Requests": "1",
    'user-agent': user
}

checkin = requests.post(url,headers=header,data=json.dumps({'content': "1"}))
print(re.findall("你已经.{10}",checkin.text))