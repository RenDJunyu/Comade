import requests

user="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.43"

checkiurl="https://www.luogu.com.cn/index/ajax_punch"
refer="https://www.luogu.com.cn/"
cookie="UM_distinctid=17526de97c73b0-0fa9014fe00a8-5b35124b-144000-17526de97c8ca5; __client_id=b1e071fcf41e5e0ec20f905db61ffb67f2e427bb; CNZZDATA5476811=cnzz_eid%3D168136113-1602672116-%26ntime%3D1603405218; login_referer=https%3A%2F%2Fwww.luogu.com.cn%2F; _uid=246367"
check = requests.get(checkiurl,headers={'user-agent':user,'cookie':cookie})
print(check.text)