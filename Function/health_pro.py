import requests,time,datetime,json,re,os
import pytesseract,hashlib
from PIL import Image

APIurl="https://healthreport.zju.edu.cn/ncov/wap/default/code"
referer="https://healthreport.zju.edu.cn/ncov/wap/default/index?ticket=ST-10274436-IJ1GWBknUfS0pZrCF9Z9-zju.edu.cn"
# :authority: healthreport.zju.edu.cn
# :path: /ncov/wap/default/code
# :method: GET
# :scheme: https

User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
cookie1= "_ga=GA1.3.1692997792.1648882713; BSFIT_oj80x=m3Tav0bImdVE93V59M,m0xW9WTwm0Mamo; BSFIT_7s6tp=; UUkey=34d109ee67c6a72d2f7eb7130d10eb45; BSFIT_tn3yB=; BSFIT_tknwv=GN108NLd8Nfemzte8t,GwvPGwLMGwtPmM; BSFIT_7lvAj=F4KRH4gQH4wzFAxW6J,FAj1HA8JFA8QFg; BSFIT_hug/7=5R1c3RJY5RGdBRhx3I,5/hcB/5V5/Ed5I,5/hcB/5V5/Ed5I; BSFIT_k06hj=qv/1qhkL9ErG9Eq3qK,qhk2qEqKqhrG9g; BSFIT_tyh7A=; BSFIT_ty7n+=; BSFIT_j4kuq=hLW1huhXhzlXhLjX6a,huqB6LlahutT6t; BSFIT_onkgr=4BN14gsxLBs04Br0qs,4go0Lgow4gNJ4D,4go0qeow4gGwqs,4go0qesw4gDFqw; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1649569878,1650170415,1650537656; BSFIT_jwi67=; BSFIT_i0k62=; BSFIT_uyktm=2hjd2tjLvtZa2Gp4wu,2tmd2tmR2tCavR,2tmB2buR2hmR2q; BSFIT_ty2B4=wFR1wBePwB03CjQLCM,wB4LwjeMwBRH7t; BSFIT_i+yu4=HGR1HugPKGiXjzT0Hi,Hu4PjGiXHuA1jX; BSFIT_/l6Ai=; BSFIT_sA4Cy=/vWG/vyYnCWSuC/Gng,/CsfnCsK/C/D/s; BSFIT_xtkvg=yJGLyJgfyvELqjx2yE,yvgbqjgwyvhfqx,yvgbqjEwyv40qE,yvgbqjEwyv4fux,yvgbqjEwyvGLqw,yvgbqjYwyvswyh,yvgbqjYwyvs2yx; BSFIT_hojBi=5rEa5r9XpftXpBhzmh,5BixmBhd5B9dph; BSFIT_motx+=; BSFIT_zm5By=GlFfGlFZIlL3GlzZIL,GBzdsjzWGBi2IL,GByZIBFWGB+dsQ; BSFIT_1y+Ck=BhPVBh9QBC14BC92BL,BCkMBC9WBCKWBd; BSFIT_rl0mq=DR1ZDRgIizg5DzC2N/,Dmr2DmrwDmxeDr; BSFIT_yvg3A=; eai-sess=olnp0g6hinlr0eh4phqtqt2mo7; _csrf=S8mwplVi9KWoF2WQ0TlCeAoMHKWf8g78bcjNEAsoc1Q%3D; _pv0=jeSX5mBmH0%2FrGY2rnb5pSgTW7uf4hx02UGDy9BhbwQtqPdHFsG4XSqnivnOzxzjrzmcUvttsfzpOm0jTIBjPpnlvUfmxY5i46jFzk3cEP0DhV13YycptI1QDPE%2B34P0GAeRZfXrEqvTMwBBvx8tt34LWSCcFdft7lVnw7T1KLyWh8Vk2FWAVtV%2FjyjjNG8XxbKzF7WGVnNAbsPbGR8UkZVSuWqDkeD%2ByFWzkUEVnrq72xl8TU6UT%2F3WUVTWNGtYQraDnr2eUCllwVCu5el8va%2FFFOgrcne6UGAAKl1DCWEKypjk9gdTLwvsxXbRmFd7WsI8r3b0g2Aw6SsZXcp6W%2BUtiol54mwmTngYWw%2BMpM4Lclg8qIzhu35xBBy0Bbkp9wekJeBocp%2Fqt7ma8GDFavo%2BnASrdPqhP2RbL8uHbMNk%3D; _pf0=XPGdd3VZpOyN9Uz%2BsXBdH4sEoA%2FIvzt8ogJ6yaDsPcQ%3D; _pc0=D6pQppquhujDEEGHfa86bTZp%2FXGvYIXQIM3ammhfuI6SKIu3rgwmPx9iMJPQklRk; iPlanetDirectoryPro=VQv6R9WHMVS8P09tfyyj0035mCeihmi277t2d2azrPfJhM0tB2Bktho4bd1zlDfXCn7%2F7F1WzwEyvGuGRjxu%2BOduprxsqVvPvDTO5GbLPwEz24GgOJbXYuzjtE8WwFhi4cvYFhT0OdU2%2BVj1uXXktfQBvvlhImurAPeQMQ0X6o6HmQ%2BrYKNu5epqtTLDh1vbS0hFQKRRjfLiqDMFaNrb9PU5%2FuL16FcDLM9%2B2S3LNPhDX2LeQKw2tHkcYvE9dwg%2F23cdwiTzX5kE0gmv%2Byt1JbQjOv1%2BVtQ66dlV1wnawCro0umsVyF7F9MZWRFHsqWWu6TtXO7lRr7jKC%2B0Z9blo7e2dEGuHEOqm1pwP8U7WTEAgNM7wUsvwvAzN3UZVNiAifwaNljHZluyq5Fm5xpAxA%3D%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1652012453; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1652012484"

APIheaders={
    "cookie":cookie1,
    "referer":referer,
    "accept": "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Microsoft Edge\";v=\"101\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin"
}

def clear_image(image):
    image = image.convert('RGB')
    width = image.size[0]
    height = image.size[1]
    noise_color = get_noise_color(image)
    
    for x in range(width):
        for y in  range(height):
            #清除边框和干扰色
            rgb = image.getpixel((x, y))
            if (x == 0 or y == 0 or x == width - 1 or y == height - 1 
                or rgb == noise_color or rgb[1]>100):
                image.putpixel((x, y), (255, 255, 255))
    return image

def get_noise_color(image):
    for y in range(1, image.size[1] - 1):
        # 获取第2列非白的颜色
        (r, g, b) = image.getpixel((2, y))
        if r < 255 and g < 255 and b < 255:
            return (r, g, b)

def get_code(num=None,cookie=cookie1):
    APIheaders['cookie']=cookie
    APIget=requests.get(APIurl,headers=APIheaders)
    # print(APIget.json())
    if num==None:
        valpng=open("valcode.png","wb")
    else:
        valpng=open("valcode/valcode"+str(num)+".png","wb")
    valpng.write(APIget.content)
    valpng.close()

    image = Image.open('valcode.png')
    # image = clear_image(image)
    #转化为灰度图
    imgry = image.convert('L')
    code = pytesseract.image_to_string(imgry,lang="eng")
    # code = pytesseract.image_to_string(imgry)
    # os.remove('Function/valcode.png')
    code=re.findall("[A-Z]",code)
    if len(code)==4:
        return code[0]+code[1]+code[2]+code[3]
    else :return get_code()


if __name__=="__main__":
    mode=3
    # for i in range(100):
    #     get_code(i)
    res=get_code()
    print(res)