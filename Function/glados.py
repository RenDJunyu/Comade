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

cookie="_ga=GA1.2.1808247846.1651036843; _gid=GA1.2.2080806569.1651036843; __stripe_mid=45be2a2a-ead7-472c-848f-b25b7cf669a977ba14; koa:sess=eyJ1c2VySWQiOjEwMzM0NywiX2V4cGlyZSI6MTY3Njk2MzU4ODMzOSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=mjQK2MTGnIsKkPLrutqOgX14PEs; _gat_gtag_UA_104464600_2=1"
header['cookie']=cookie
checkin = requests.post(url1,headers=header,data=json.dumps({'token': "glados_network"}))
state = requests.get(url2,headers={'accept':accept,'referer': referer,'user-agent':user2,'cookie': cookie})
print(re.findall(r"\"message\":\"[^\"]*\"",checkin.text))
print(re.findall(r"\"leftDays\":\"[^\"]*\"",state.text))
checkdetail=re.findall(":checkin:[\d-]*",checkin.text)
for i in range(min(30,len(checkdetail))):
    print(checkdetail[i][1:])

cookie="_ga=GA1.2.537804143.1648303569; koa:sess=eyJ1c2VySWQiOjEzNTg3MCwiX2V4cGlyZSI6MTY3NTQ5MTc5MjMzNSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=8shtY5c9WEgIiKWtkDVKMc7n88E; _gid=GA1.2.255055262.1651036881; _gat_gtag_UA_104464600_2=1"
header['cookie']=cookie
checkin = requests.post(url1,headers=header,data=json.dumps({'token': "glados_network"}))
state = requests.get(url2,headers={'accept':accept,'referer': referer,'user-agent':user2,'cookie': cookie})
print(re.findall(r"\"message\":\"[^\"]*\"",checkin.text))
print(re.findall(r"\"leftDays\":\"[^\"]*\"",state.text))
checkdetail=re.findall(":checkin:[\d-]*",checkin.text)
for i in range(min(30,len(checkdetail))):
    print(checkdetail[i][1:])