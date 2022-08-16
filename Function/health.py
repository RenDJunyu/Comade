import requests
import re
# from health_pro import get_code

headers={
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-length": "2289",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "",
    "origin": "https://healthreport.zju.edu.cn",
    "referer": "https://healthreport.zju.edu.cn/ncov/wap/default/index?from=history",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
referer = 'https://healthreport.zju.edu.cn/ncov/wap/default/index?from=history'
loclist=["120.125568305122","30.269340549046"]#school
submiturl='https://healthreport.zju.edu.cn/ncov/wap/default/save'

locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")

data={
    # "verifyCode": get_code(cookie=cookie),
    "sfzx":"1","sfjcwhry":"0","sfcyglq":"0","sftjwh":"0","sftjhb":"0","bztcyy":"0","fjsj":"0","created_uid":"0","sfjchbry":"0","sfsfbh":"0",
    "jhfjsftjwh":"0","jhfjsftjhb":"0","szsqsfybl":0,"sfsqhzjkk":"1","sqhzjkkys":"1","sfygtjzzfj":0,"sfymqjczrj":"0","sfyrjjh":"0","nrjrq":"0",
    "rjjtfs1":"0","jnjtfs1":"0","sfqrxxss":"1","sffrqjwdg":"0","sfqtyyqjwdg":"0","sfhsjc":"1","zgfx14rfh":"0","sfyxjzxgym":"1",
    "sfbyjzrq":"5","jzxgymqk":"6","campus":"\u7389\u6cc9\u6821\u533a","internship":"2",
    'address': loctext[loctext.index("formatted_address")+2],
    'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
    'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
    'province': loctext[loctext.index("province")+2],
    'city': loctext[loctext.index("city")+2],
}
# print(loctext[loctext.index("formatted_address")+2])

cookie="_ga=GA1.3.1720262211.1602687713; eai-sess=6serm2rujdf07bg3n8iftc0ba4; UUkey=916d7bd103a4f2fdbfa761e07ef09ca8; Hm_lvt_48b682d4885d22a90111e46b972e3268=1603201784,1603252182,1603407288; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1603407288"
#loclist=["107.45307","31.214935"]#home

headers["cookie"]=cookie
locget = requests.post(submiturl,data=data,headers=headers)
res=locget.json()['m']
print(res)

cookie="eai-sess=s4ng1njate3ptkfh6bkmsrc115; UUkey=b8f8156f7a65b37aa795cf4f7d61e9e0; _csrf=S8mwplVi9KWoF2WQ0TlCeFkhpR4lX1aJpoKgE2bhNX0%3D; _pv0=XRJlKUFMl2way3Zh6ZasvwUpdKno8L2FgghT2TAzUhzArWjlkn2N4xGmspk1JczgQzmxKOKFsVWJEmzcSHl%2FOX8BHYKiN6juLfyBPudRLkdQ4FlhUVivCfITkqg6YeD0iy6KMxI4RYKvloELvXgAVOabthpHYDwI2YtK0IinOJ%2FpIM%2BDBL3d51ziVVbfpM8vSbVXPbS9IfVOlOcXlQaNRfATVJWJTJx0hpMPny1wD9GJYG7tx1bhFSwjndKzfIE0Xib8vD9zt2JB52t8VfOOdyNGJOHFDIrhXXu%2Fi5Tyr2Lve7I6J2c%2Fynaw8T%2BBK3WBFePoFBqaJgYv1QX%2FhhccJL5ae4O2aqHz76C9DL71xUi0aQM8aYtC2E4spd%2BDr6F0KvHFet%2FOhkEKLRbjNU1ggUmO3mKO5M1LVNA7eDuaIvU%3D; _pf0=0xYOwppE7LKdiKaI8y69n1HYMYAAfdlvDe3GQKv5%2FsI%3D; _pc0=cjkYca4h2r1qV4GDJr2gv5di5ZCuHwCrqraB38kofv88QqqFw0cqLUPUdBj1tPPa; iPlanetDirectoryPro=0UC4LcbQU97EayPsiO%2B4Y9o50qkNPifkka2yyn83Cfl6BeN6KTOj%2BKWusRAqhgm9NBjF%2By0ISGuTEm22BYuHBijGLYj01A0CUlguRWffRXaAWggHn5iwMcYTLbtIi03XSDX98fjuv8YVPVh65PBOIVP3WdhKpQNtpD5k3BHaUdR%2FItJf5TLxDmAvbTUWsCA%2F%2BJUCpa%2Bp6Q4Dglj6%2FQuyQdcjcqXrO2N1ifNGB4NHp4MXfiWDD5Q9iXirc1s2qtmWARzxSWvCchA%2F9uHhiy4%2FkX1dUpjqoQckQYo2Zf8myRIBrBs%2FoZsY%2FAV7oI571rKSdc6iUxt8c1A3Bpc26ZMYsgdhWDiS9LmEGtlCCJiv%2Byo%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1613312088; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1613312125"
#loclist=["120.9806","28.0722"]#cwx

headers["cookie"]=cookie
locget = requests.post(submiturl,data=data,headers=headers)
res=locget.json()['m']
print(res)

cookie="_ga=GA1.3.333087132.1615362891; UUkey=0657e401ba9cfeddfbe3f320e901caa0; Hm_lvt_fe30bbc1ee45421ec1679d1b8d8f8453=1621044720; UM_distinctid=17b595e1a2d3cb-00fb08f0da275d-7868786b-384000-17b595e1a2e5a7; eai-sess=890s4pffhfhscc3l0giecvfa56; _csrf=S8mwplVi9KWoF2WQ0TlCeNO7RkVn2lC46wVDJ6pkd1k=; _pv0=vUB5UbRLzmisU1yoPwnHH1h0eMhEnlGSfOwsu3/M20glp/d2ttwUt17+zNvk3XzNQ+76V0aM9owgysha5mN71VtHMlLV5dMxG9qNefmfnTeWAsRImSJvmzYVd4G10Nwo+F1xBrJJFq7Mm2xZ2IiqnSr5+Y8LnvX9cwcPGWcLBOOJNeLrnBXOlRXjrJcPLeje138efvNfdBK6z4dnt2co9tnbus1hOisLW9vByy6KNeb5PjrqI43tXstZb1bWvW8CaEB5gRlNX7jEIMU4GkJSkakfGDg2gFeM2i4+6wNYJQ7r9I1T+50D6usBn5MzI/GIASuNHc0tCRl/9ed5uoo6joDAf6GS8iDBa+or2o7AZOJkZTRyw+XxZrgsxlgtpWwzastpGwJ2kbgYaQAbqeG23cWUVywgbofcoONctgjxAcI=; _pf0=jc1ArDrIT21ne6A8floiFdgVqgXwaAQDYJTOJa6z6cs=; _pc0=TW+XtGdIrpk2rQq6Fd4+xOJ6+PT0bYDKwEYC2ds6sT4Ur863vmkNd+3oDgYv6EnK; iPlanetDirectoryPro=8PaPRGdaYOJ/nZZeNh2hrsz4AiXSmn/ApiOVmVL1fNdGwnTrEllyHEFQExOnX/OiULR59PjGIXJ41L6nZELQM3vvTuytgkOh8vxnEVwUVaLIwe6EdVy7qPlLswcwTIGGr8P8duUmxvDYLhtdLevMW4uDqrSp9fgHafFBHmLqXdUa86UaSl61KuAfbfliSNa6qALU+NJgAGpzzM9jUIvKQZs4A0+hgxMvMxSp75dpxuOyZKrqQdY9VAZLRpvgShk/Wxft2P1jV8M6Ddgtrfx3kR0d69ie5+9gpkwZxwfvmXOdOctfRrMG37fkXVYbv6mr22lFchDooerqNnYkGq4GOAVfK4MYPhTx5yBf/E8fC84hO4gHvvGhZvQyTXx+V0qW; Hm_lvt_48b682d4885d22a90111e46b972e3268=1629799752,1629799760; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1629799785"
#loclist=[" "," "]#jyt

headers["cookie"]=cookie
locget = requests.post(submiturl,data=data,headers=headers)
res=locget.json()['m']
print(res)

cookie="eai-sess=smp79fp631alc29agipctoalf3; UUkey=6a4032373ce12a9f7aa71f7f98d7825d; _csrf=S8mwplVi9KWoF2WQ0TlCeF1JGS82wucvkhsp3R10a%2Fw%3D; _pv0=mfbFV6AHRlSjYaH60BHOc1Xv70%2Bort9Jf5uKNDDW9CM%2BKKz978t7NsXSZOmR0bH97dnEmpZA1OjLfxy%2BWh1Qw%2Ff1BpOKB44Af4y5HRQqyOvk0rDyjcQLK3bM1m%2FQ0nQcwGxWzpUrSftoElyeEZiXTdZgxFV7oI9NCjygQFtg0JEOjyA4szgQcXKnQIYhpqfKcABtjd3C%2B5J%2FK%2Bam2UBJcz0DE%2FzItH0irqm9zQjdhNZTKywiEQpw9qgDsfpV3mlCf8g2pzN6lAhDQpBWL8%2BrgM1cFLLBNMR0Fgock2kqp%2FzhsOPe6kBQx8E2jL15tcmKS8MK2H547Bq3vlUa6IjYgTELv1h5Jk1E2ik1LlYLkmDVjSaD99XYtijO02KsMwtjo7zDpd0UDLDwUATinyuso986NBhWd4undXQLcVfBVQ4%3D; _pf0=w2nj2GuKO27LiX94o2SmPP1iRxeoQU7FTfL%2BuwpOi0c%3D; _pc0=LovLvnlfs%2BVHLrtT%2BE9jLH%2F%2BL1Hf6fzJTZJ0UkNLK6VkdTq6FpWBzFcAx46soLpQ; iPlanetDirectoryPro=g7QMBKN2VCzvMQMSNJm3F%2BS6beGfgrczn6VT%2B4ppkKQjOWBN1kIuSXa4sVtKwBGvwxw6msXjwtThBi1N6Iousgi2KyqZaEuWM6hpEg41MwDsyl8gZZmvbFNr7Mm9LlKqkRm7M4LzwUeWVQIFpSjSyi5kfTBD7V1I8S0TIQPM9ck6Cf0y9hfDGhdPManvfbaqagAOLoFgsSTpBJXnZ%2BWOPw2LBsPTR763HdmRbiJHBVZ2mHn5hgpJ%2BH68Y3Zadddr9k9loq%2BCNxR9AhPlu90mzRH7Fe2Td7CYLcH5N9wysQnIYnuDe2Dwgyu4ttHb4hRx0wo1heIAyHH4l6JI6QQNNlKegmNaDycqxYsr7ymi8kI%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1645008879; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1645008879"
#loclist=[" "," "]#gxs

headers["cookie"]=cookie
locget = requests.post(submiturl,data=data,headers=headers)
res=locget.json()['m']
print(res)

cookie="_ga=GA1.3.1994190377.1592554949; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1652886165; eai-sess=j7ea3gb83v3uusr0sds5g9ait4; UUkey=97b71b97e5b2ab23a0ea3f2364972794; _csrf=S8mwplVi9KWoF2WQ0TlCeCNkacbzbf5Viu%2F5yMblFvA%3D; _pv0=5liAmpO7PItbBIWWKWI6iXzd%2BxhWcgjEbLyccuOE0o9VBgYLO3WUx78dMkmOw2QYVHWyB%2FWAAE0dwLWtbFdbJoOP2YkQsEn2BPbf%2BA1xyAFCHMuFMmG5rF%2BZD2ML0brV2gPJurJpAS3m7cRoYRl6aOnl%2F0vCsIZXK59rSArFpiDj%2FbcOlCch8POA3yTSu9zvbOgesNSBsi6IP2shhmeG46wrypOSA0h0aFKLyhrKIMi8vBsKMrFIgnDZNBrnPXNkHKJRpT06IwTAYU4V%2BYSLg%2FqavpzWvGT2j%2B76v3TqALly8uGnNBLuJ%2BcaflQiK5DnWJGeuaqA%2B3RKkGVnK3TxJuGUISazWKeUEbK6hbz%2BkymABayoHr3%2F9EW0L5beSqHM93jd4gs6lsZaeO0BQZBM3dlNuVmNS3IIr1zx8A0T%2Fe4%3D; _pf0=gDksGFW7BA5gaCh%2B6N5nLXU%2BWASzpMN00lrk4qF5nls%3D; _pc0=LyrkC5TQTK71GPh0A40MWDnpPP7Vy8QQ34uNc12DUIFxrnI9IhdFeqrwva0ltwX2; iPlanetDirectoryPro=UdYk0I9HjXxz0QYuM3kpAUqdoRggd2Npcz43wcfwLHy%2B0GH6EFKwyvzWVrxxuMWSw8vJIywai0AkJqyAcFjX5MtKI2RdpZQw11dNZMUgpVbtcYrdoGzGRM8Z6%2BZZ1uVN%2Ff7stD4LiZL6bjf0hxzPpkhZVEUlYPdPoaRUfmpxqgKhQbI64KDkZBolHkrqyQp81IvVH428WDf5PHZg9ZuYEhhDGrA9aqmY0zyWj4NFHWMjF9iXVNMY69K7r52jSNxpvTNKIHN3yKg46%2Fi4%2F7ulkOnjk8o2mETVZSje6gzgZPi2zy5l1bHqA3opkW5Jwrv5%2F6O6zHq1SqkRqKaDXV422si0oB3UPIBG3V0h3cHOM%2F3gRu9%2FnG6LZaI2wHmH6zWqNCegSgpR7NMNJ%2BO6XVtDhQ%3D%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1656292872; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1656292872"
#loclist=[" "," "]#ssy

headers["cookie"]=cookie
locget = requests.post(submiturl,data=data,headers=headers)
res=locget.json()['m']
print(res)
