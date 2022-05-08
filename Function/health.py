import requests
import re
from health_pro import get_code

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

cookie="_ga=GA1.3.1720262211.1602687713; eai-sess=6serm2rujdf07bg3n8iftc0ba4; UUkey=916d7bd103a4f2fdbfa761e07ef09ca8; Hm_lvt_48b682d4885d22a90111e46b972e3268=1603201784,1603252182,1603407288; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1603407288"
# cookie= "_ga=GA1.3.1692997792.1648882713; BSFIT_oj80x=m3Tav0bImdVE93V59M,m0xW9WTwm0Mamo; BSFIT_7s6tp=; UUkey=34d109ee67c6a72d2f7eb7130d10eb45; BSFIT_tn3yB=; BSFIT_tknwv=GN108NLd8Nfemzte8t,GwvPGwLMGwtPmM; BSFIT_7lvAj=F4KRH4gQH4wzFAxW6J,FAj1HA8JFA8QFg; BSFIT_hug/7=5R1c3RJY5RGdBRhx3I,5/hcB/5V5/Ed5I,5/hcB/5V5/Ed5I; BSFIT_k06hj=qv/1qhkL9ErG9Eq3qK,qhk2qEqKqhrG9g; BSFIT_tyh7A=; BSFIT_ty7n+=; BSFIT_j4kuq=hLW1huhXhzlXhLjX6a,huqB6LlahutT6t; BSFIT_onkgr=4BN14gsxLBs04Br0qs,4go0Lgow4gNJ4D,4go0qeow4gGwqs,4go0qesw4gDFqw; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1649569878,1650170415,1650537656; BSFIT_jwi67=; BSFIT_i0k62=; BSFIT_uyktm=2hjd2tjLvtZa2Gp4wu,2tmd2tmR2tCavR,2tmB2buR2hmR2q; BSFIT_ty2B4=wFR1wBePwB03CjQLCM,wB4LwjeMwBRH7t; BSFIT_i+yu4=HGR1HugPKGiXjzT0Hi,Hu4PjGiXHuA1jX; BSFIT_/l6Ai=; BSFIT_sA4Cy=/vWG/vyYnCWSuC/Gng,/CsfnCsK/C/D/s; BSFIT_xtkvg=yJGLyJgfyvELqjx2yE,yvgbqjgwyvhfqx,yvgbqjEwyv40qE,yvgbqjEwyv4fux,yvgbqjEwyvGLqw,yvgbqjYwyvswyh,yvgbqjYwyvs2yx; BSFIT_hojBi=5rEa5r9XpftXpBhzmh,5BixmBhd5B9dph; BSFIT_motx+=; BSFIT_zm5By=GlFfGlFZIlL3GlzZIL,GBzdsjzWGBi2IL,GByZIBFWGB+dsQ; BSFIT_1y+Ck=BhPVBh9QBC14BC92BL,BCkMBC9WBCKWBd; BSFIT_rl0mq=DR1ZDRgIizg5DzC2N/,Dmr2DmrwDmxeDr; BSFIT_yvg3A=; eai-sess=olnp0g6hinlr0eh4phqtqt2mo7; _csrf=S8mwplVi9KWoF2WQ0TlCeAoMHKWf8g78bcjNEAsoc1Q%3D; _pv0=jeSX5mBmH0%2FrGY2rnb5pSgTW7uf4hx02UGDy9BhbwQtqPdHFsG4XSqnivnOzxzjrzmcUvttsfzpOm0jTIBjPpnlvUfmxY5i46jFzk3cEP0DhV13YycptI1QDPE%2B34P0GAeRZfXrEqvTMwBBvx8tt34LWSCcFdft7lVnw7T1KLyWh8Vk2FWAVtV%2FjyjjNG8XxbKzF7WGVnNAbsPbGR8UkZVSuWqDkeD%2ByFWzkUEVnrq72xl8TU6UT%2F3WUVTWNGtYQraDnr2eUCllwVCu5el8va%2FFFOgrcne6UGAAKl1DCWEKypjk9gdTLwvsxXbRmFd7WsI8r3b0g2Aw6SsZXcp6W%2BUtiol54mwmTngYWw%2BMpM4Lclg8qIzhu35xBBy0Bbkp9wekJeBocp%2Fqt7ma8GDFavo%2BnASrdPqhP2RbL8uHbMNk%3D; _pf0=XPGdd3VZpOyN9Uz%2BsXBdH4sEoA%2FIvzt8ogJ6yaDsPcQ%3D; _pc0=D6pQppquhujDEEGHfa86bTZp%2FXGvYIXQIM3ammhfuI6SKIu3rgwmPx9iMJPQklRk; iPlanetDirectoryPro=VQv6R9WHMVS8P09tfyyj0035mCeihmi277t2d2azrPfJhM0tB2Bktho4bd1zlDfXCn7%2F7F1WzwEyvGuGRjxu%2BOduprxsqVvPvDTO5GbLPwEz24GgOJbXYuzjtE8WwFhi4cvYFhT0OdU2%2BVj1uXXktfQBvvlhImurAPeQMQ0X6o6HmQ%2BrYKNu5epqtTLDh1vbS0hFQKRRjfLiqDMFaNrb9PU5%2FuL16FcDLM9%2B2S3LNPhDX2LeQKw2tHkcYvE9dwg%2F23cdwiTzX5kE0gmv%2Byt1JbQjOv1%2BVtQ66dlV1wnawCro0umsVyF7F9MZWRFHsqWWu6TtXO7lRr7jKC%2B0Z9blo7e2dEGuHEOqm1pwP8U7WTEAgNM7wUsvwvAzN3UZVNiAifwaNljHZluyq5Fm5xpAxA%3D%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1652012453; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1652012484"
#loclist=["107.45307","31.214935"]#home
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"

locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
while 1:
    data={
        "verifyCode": get_code(cookie=cookie),
        "sfymqjczrj": "0",  "sfyrjjh": "0",     "nrjrq": "0",       "rjjtfs1": "0",     "jnjtfs1": "0",
        "sfqrxxss": "1",    "sfqtyyqjwdg": "0", "sffrqjwdg": "0",   "sfhsjc": "1",      "zgfx14rfh": "0",
        "sfyxjzxgym": "1",  "sfbyjzrq": "5",    "jzxgymqk": "6",    "campus": "玉泉校区","ismoved": "0",
        "tw": "0",          "sfcxtz": "0",      "sfjcbh": "0",      "sfcxzysx": "0",    "sfyyjc": "0","jcjgqr": "0",
        "sfzx": "1",        "sfjcwhry": "0",    "sfjchbry": "0",    "sfcyglq": "0",     "bztcyy": "0",
        "sftjhb": "0",      "sftjwh": "0",      "sfyqjzgc": "0",    "sfsqhzjkk": "1",   "sqhzjkkys": "1",
        "szsqsfybl": "0",
        'address': loctext[loctext.index("formatted_address")+2],
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
        'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
        'province': loctext[loctext.index("province")+2],
        'city': loctext[loctext.index("city")+2],
    }
    # print(loctext[loctext.index("formatted_address")+2])
    headers["cookie"]=cookie
    locget = requests.post(submiturl,data=data,headers=headers)
    res=locget.json()['m']
    if not res=="验证码错误":
        print("成功")
        break

cookie="eai-sess=s4ng1njate3ptkfh6bkmsrc115; UUkey=b8f8156f7a65b37aa795cf4f7d61e9e0; _csrf=S8mwplVi9KWoF2WQ0TlCeFkhpR4lX1aJpoKgE2bhNX0%3D; _pv0=XRJlKUFMl2way3Zh6ZasvwUpdKno8L2FgghT2TAzUhzArWjlkn2N4xGmspk1JczgQzmxKOKFsVWJEmzcSHl%2FOX8BHYKiN6juLfyBPudRLkdQ4FlhUVivCfITkqg6YeD0iy6KMxI4RYKvloELvXgAVOabthpHYDwI2YtK0IinOJ%2FpIM%2BDBL3d51ziVVbfpM8vSbVXPbS9IfVOlOcXlQaNRfATVJWJTJx0hpMPny1wD9GJYG7tx1bhFSwjndKzfIE0Xib8vD9zt2JB52t8VfOOdyNGJOHFDIrhXXu%2Fi5Tyr2Lve7I6J2c%2Fynaw8T%2BBK3WBFePoFBqaJgYv1QX%2FhhccJL5ae4O2aqHz76C9DL71xUi0aQM8aYtC2E4spd%2BDr6F0KvHFet%2FOhkEKLRbjNU1ggUmO3mKO5M1LVNA7eDuaIvU%3D; _pf0=0xYOwppE7LKdiKaI8y69n1HYMYAAfdlvDe3GQKv5%2FsI%3D; _pc0=cjkYca4h2r1qV4GDJr2gv5di5ZCuHwCrqraB38kofv88QqqFw0cqLUPUdBj1tPPa; iPlanetDirectoryPro=0UC4LcbQU97EayPsiO%2B4Y9o50qkNPifkka2yyn83Cfl6BeN6KTOj%2BKWusRAqhgm9NBjF%2By0ISGuTEm22BYuHBijGLYj01A0CUlguRWffRXaAWggHn5iwMcYTLbtIi03XSDX98fjuv8YVPVh65PBOIVP3WdhKpQNtpD5k3BHaUdR%2FItJf5TLxDmAvbTUWsCA%2F%2BJUCpa%2Bp6Q4Dglj6%2FQuyQdcjcqXrO2N1ifNGB4NHp4MXfiWDD5Q9iXirc1s2qtmWARzxSWvCchA%2F9uHhiy4%2FkX1dUpjqoQckQYo2Zf8myRIBrBs%2FoZsY%2FAV7oI571rKSdc6iUxt8c1A3Bpc26ZMYsgdhWDiS9LmEGtlCCJiv%2Byo%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1613312088; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1613312125"
#loclist=["120.9806","28.0722"]#cwx
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
while 1:
    data={
        "verifyCode": get_code(cookie=cookie),
        "sfymqjczrj": "0",  "sfyrjjh": "0",     "nrjrq": "0",       "rjjtfs1": "0",     "jnjtfs1": "0",
        "sfqrxxss": "1",    "sfqtyyqjwdg": "0", "sffrqjwdg": "0",   "sfhsjc": "1",      "zgfx14rfh": "0",
        "sfyxjzxgym": "1",  "sfbyjzrq": "5",    "jzxgymqk": "6",    "campus": "玉泉校区","ismoved": "0",
        "tw": "0",          "sfcxtz": "0",      "sfjcbh": "0",      "sfcxzysx": "0",    "sfyyjc": "0","jcjgqr": "0",
        "sfzx": "1",        "sfjcwhry": "0",    "sfjchbry": "0",    "sfcyglq": "0",     "bztcyy": "0",
        "sftjhb": "0",      "sftjwh": "0",      "sfyqjzgc": "0",    "sfsqhzjkk": "1",   "sqhzjkkys": "1",
        "szsqsfybl": "0",
        'address': loctext[loctext.index("formatted_address")+2],
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
        'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
        'province': loctext[loctext.index("province")+2],
        'city': loctext[loctext.index("city")+2],
    }
    headers["cookie"]=cookie
    locget = requests.post(submiturl,data=data,headers=headers)
    res=locget.json()['m']
    if not res=="验证码错误":
        print("成功")
        break

cookie="_ga=GA1.3.333087132.1615362891; UUkey=0657e401ba9cfeddfbe3f320e901caa0; Hm_lvt_fe30bbc1ee45421ec1679d1b8d8f8453=1621044720; UM_distinctid=17b595e1a2d3cb-00fb08f0da275d-7868786b-384000-17b595e1a2e5a7; eai-sess=890s4pffhfhscc3l0giecvfa56; _csrf=S8mwplVi9KWoF2WQ0TlCeNO7RkVn2lC46wVDJ6pkd1k=; _pv0=vUB5UbRLzmisU1yoPwnHH1h0eMhEnlGSfOwsu3/M20glp/d2ttwUt17+zNvk3XzNQ+76V0aM9owgysha5mN71VtHMlLV5dMxG9qNefmfnTeWAsRImSJvmzYVd4G10Nwo+F1xBrJJFq7Mm2xZ2IiqnSr5+Y8LnvX9cwcPGWcLBOOJNeLrnBXOlRXjrJcPLeje138efvNfdBK6z4dnt2co9tnbus1hOisLW9vByy6KNeb5PjrqI43tXstZb1bWvW8CaEB5gRlNX7jEIMU4GkJSkakfGDg2gFeM2i4+6wNYJQ7r9I1T+50D6usBn5MzI/GIASuNHc0tCRl/9ed5uoo6joDAf6GS8iDBa+or2o7AZOJkZTRyw+XxZrgsxlgtpWwzastpGwJ2kbgYaQAbqeG23cWUVywgbofcoONctgjxAcI=; _pf0=jc1ArDrIT21ne6A8floiFdgVqgXwaAQDYJTOJa6z6cs=; _pc0=TW+XtGdIrpk2rQq6Fd4+xOJ6+PT0bYDKwEYC2ds6sT4Ur863vmkNd+3oDgYv6EnK; iPlanetDirectoryPro=8PaPRGdaYOJ/nZZeNh2hrsz4AiXSmn/ApiOVmVL1fNdGwnTrEllyHEFQExOnX/OiULR59PjGIXJ41L6nZELQM3vvTuytgkOh8vxnEVwUVaLIwe6EdVy7qPlLswcwTIGGr8P8duUmxvDYLhtdLevMW4uDqrSp9fgHafFBHmLqXdUa86UaSl61KuAfbfliSNa6qALU+NJgAGpzzM9jUIvKQZs4A0+hgxMvMxSp75dpxuOyZKrqQdY9VAZLRpvgShk/Wxft2P1jV8M6Ddgtrfx3kR0d69ie5+9gpkwZxwfvmXOdOctfRrMG37fkXVYbv6mr22lFchDooerqNnYkGq4GOAVfK4MYPhTx5yBf/E8fC84hO4gHvvGhZvQyTXx+V0qW; Hm_lvt_48b682d4885d22a90111e46b972e3268=1629799752,1629799760; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1629799785"
#loclist=[" "," "]#jyt
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
while 1:
    data={
        "verifyCode": get_code(cookie=cookie),
        "sfymqjczrj": "0",  "sfyrjjh": "0",     "nrjrq": "0",       "rjjtfs1": "0",     "jnjtfs1": "0",
        "sfqrxxss": "1",    "sfqtyyqjwdg": "0", "sffrqjwdg": "0",   "sfhsjc": "1",      "zgfx14rfh": "0",
        "sfyxjzxgym": "1",  "sfbyjzrq": "5",    "jzxgymqk": "6",    "campus": "玉泉校区","ismoved": "0",
        "tw": "0",          "sfcxtz": "0",      "sfjcbh": "0",      "sfcxzysx": "0",    "sfyyjc": "0","jcjgqr": "0",
        "sfzx": "1",        "sfjcwhry": "0",    "sfjchbry": "0",    "sfcyglq": "0",     "bztcyy": "0",
        "sftjhb": "0",      "sftjwh": "0",      "sfyqjzgc": "0",    "sfsqhzjkk": "1",   "sqhzjkkys": "1",
        "szsqsfybl": "0",
        'address': loctext[loctext.index("formatted_address")+2],
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
        'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
        'province': loctext[loctext.index("province")+2],
        'city': loctext[loctext.index("city")+2],
    }
    headers["cookie"]=cookie
    locget = requests.post(submiturl,data=data,headers=headers)
    res=locget.json()['m']
    if not res=="验证码错误":
        print("成功")
        break

cookie="eai-sess=smp79fp631alc29agipctoalf3; UUkey=6a4032373ce12a9f7aa71f7f98d7825d; _csrf=S8mwplVi9KWoF2WQ0TlCeF1JGS82wucvkhsp3R10a%2Fw%3D; _pv0=mfbFV6AHRlSjYaH60BHOc1Xv70%2Bort9Jf5uKNDDW9CM%2BKKz978t7NsXSZOmR0bH97dnEmpZA1OjLfxy%2BWh1Qw%2Ff1BpOKB44Af4y5HRQqyOvk0rDyjcQLK3bM1m%2FQ0nQcwGxWzpUrSftoElyeEZiXTdZgxFV7oI9NCjygQFtg0JEOjyA4szgQcXKnQIYhpqfKcABtjd3C%2B5J%2FK%2Bam2UBJcz0DE%2FzItH0irqm9zQjdhNZTKywiEQpw9qgDsfpV3mlCf8g2pzN6lAhDQpBWL8%2BrgM1cFLLBNMR0Fgock2kqp%2FzhsOPe6kBQx8E2jL15tcmKS8MK2H547Bq3vlUa6IjYgTELv1h5Jk1E2ik1LlYLkmDVjSaD99XYtijO02KsMwtjo7zDpd0UDLDwUATinyuso986NBhWd4undXQLcVfBVQ4%3D; _pf0=w2nj2GuKO27LiX94o2SmPP1iRxeoQU7FTfL%2BuwpOi0c%3D; _pc0=LovLvnlfs%2BVHLrtT%2BE9jLH%2F%2BL1Hf6fzJTZJ0UkNLK6VkdTq6FpWBzFcAx46soLpQ; iPlanetDirectoryPro=g7QMBKN2VCzvMQMSNJm3F%2BS6beGfgrczn6VT%2B4ppkKQjOWBN1kIuSXa4sVtKwBGvwxw6msXjwtThBi1N6Iousgi2KyqZaEuWM6hpEg41MwDsyl8gZZmvbFNr7Mm9LlKqkRm7M4LzwUeWVQIFpSjSyi5kfTBD7V1I8S0TIQPM9ck6Cf0y9hfDGhdPManvfbaqagAOLoFgsSTpBJXnZ%2BWOPw2LBsPTR763HdmRbiJHBVZ2mHn5hgpJ%2BH68Y3Zadddr9k9loq%2BCNxR9AhPlu90mzRH7Fe2Td7CYLcH5N9wysQnIYnuDe2Dwgyu4ttHb4hRx0wo1heIAyHH4l6JI6QQNNlKegmNaDycqxYsr7ymi8kI%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1645008879; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1645008879"
#loclist=[" "," "]#gxs
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
while 1:
    data={
        "verifyCode": get_code(cookie=cookie),
        "sfymqjczrj": "0",  "sfyrjjh": "0",     "nrjrq": "0",       "rjjtfs1": "0",     "jnjtfs1": "0",
        "sfqrxxss": "1",    "sfqtyyqjwdg": "0", "sffrqjwdg": "0",   "sfhsjc": "1",      "zgfx14rfh": "0",
        "sfyxjzxgym": "1",  "sfbyjzrq": "5",    "jzxgymqk": "6",    "campus": "玉泉校区","ismoved": "0",
        "tw": "0",          "sfcxtz": "0",      "sfjcbh": "0",      "sfcxzysx": "0",    "sfyyjc": "0","jcjgqr": "0",
        "sfzx": "1",        "sfjcwhry": "0",    "sfjchbry": "0",    "sfcyglq": "0",     "bztcyy": "0",
        "sftjhb": "0",      "sftjwh": "0",      "sfyqjzgc": "0",    "sfsqhzjkk": "1",   "sqhzjkkys": "1",
        "szsqsfybl": "0",
        'address': loctext[loctext.index("formatted_address")+2],
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
        'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
        'province': loctext[loctext.index("province")+2],
        'city': loctext[loctext.index("city")+2],
    }
    headers["cookie"]=cookie
    locget = requests.post(submiturl,data=data,headers=headers)
    res=locget.json()['m']
    if not res=="验证码错误":
        print("成功")
        break
