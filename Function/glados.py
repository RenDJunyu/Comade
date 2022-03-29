import requests
import json
import re

#glados
url1= "https://glados.rocks/api/user/checkin"
url2= "https://glados.rocks/api/user/status"
user1="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
user2="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
referer='https://glados.rocks/console'

cookie = "_ga=GA1.2.926605631.1615797851; koa:sess=eyJ1c2VySWQiOjU0Njk5LCJfZXhwaXJlIjoxNjU2NjcwODEyNzk0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=mL_0TbcxVtFpIZC2fJc9gy2XlBQ; _gid=GA1.2.70808319.1633856226; _gat_gtag_UA_104464600_2=1"
header={
    'authority': 'glados.rocks',
    'method': 'POST',
    'path': '/api/user/checkin',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '26',
    'content-type':'application/json;charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://glados.rocks',
    'referer': 'https://glados.rocks/console/checkin',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user1
}
checkin = requests.post(url1,headers=header,data=json.dumps({'token': "glados_network"}))
state = requests.get(url2,headers={'accept':accept,'referer': referer,'user-agent':user2,'cookie': cookie})
print(re.findall(r"\"message\":\"[^\"]*\"",checkin.text))
print(re.findall(r"\"leftDays\":\"[^\"]*\"",state.text))
checkdetail=re.findall(":checkin:[\d-]*",checkin.text)
for i in range(min(30,len(checkdetail))):
    print(checkdetail[i][1:])

cookie="_ga=GA1.2.926605631.1615797851; _gid=GA1.2.1585235980.1646478051; koa:sess=eyJ1c2VySWQiOjc2MzM0LCJfZXhwaXJlIjoxNjcyMzk4MjIyMzUzLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=viwsNjRupdQ3ZKTvKHH7Y7P2JBE; _gat_gtag_UA_104464600_2=1"
header['cookie']=cookie
checkin = requests.post(url1,headers=header,data=json.dumps({'token': "glados_network"}))
state = requests.get(url2,headers={'accept':accept,'referer': referer,'user-agent':user2,'cookie': cookie})
print(re.findall(r"\"message\":\"[^\"]*\"",checkin.text))
print(re.findall(r"\"leftDays\":\"[^\"]*\"",state.text))
checkdetail=re.findall(":checkin:[\d-]*",checkin.text)
for i in range(min(30,len(checkdetail))):
    print(checkdetail[i][1:])

#N station
host='www.nexushd.org'
origin='http://www.nexushd.org'
referer='http://www.nexushd.org/signin.php'
url= "http://www.nexushd.org/signin.php?"
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
cookie = "c_secure_uid=MTQxMzQ5; c_secure_ssl=bm9wZQ==; c_secure_tracker_ssl=bm9wZQ==; c_secure_login=bm9wZQ==; c_secure_pass=6af69e7fdf6a066a9610cc3d671a201a"

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
print(re.findall("你已经.{20}",checkin.text))