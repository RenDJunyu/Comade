import requests,time,datetime,json,re,os
import pytesseract,hashlib
from PIL import Image
stu={"Ren":["3190104963","Zhu386617588"],"Long":["3190101088","000"]}
stuid,mmcode=stu["Ren"]
mobile='19200000000'

Referer1='http://10.203.97.155/home/book/index/type/4'
Referer2='http://10.203.97.155/book/notice/act_id/1581/type/4/lib/11'
Host='10.203.97.155'
Origin='http://10.203.97.155'
cookieout="PHPSESSID=hgc95ps3lepcpmg57vheea7422"
APIurl="http://10.203.97.155/api.php/check"

User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'\
    +'537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'
Accept_Encoding='gzip, deflate, br'
Accept_Language='zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
Connection='keep-alive'

APIheaders={
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    
    'Cookie': cookieout,
    'Accept-Encoding':Accept_Encoding,
    'Accept-Language': Accept_Language,
    'Connection':Connection,
    'Host': Host,
    'Referer': Referer1,
    'User-Agent':User_Agent
}

Signinurl_old="http://10.203.97.155/api.php/login"
Signinurl="https://zjuam.zju.edu.cn/cas/login?service=http%3A%2F%2F10.203.97.155%2Fcas%2Findex.php%3Fcallback%3Dhttp%3A%2F%2F10.203.97.155%2Fhome%2Fbook%2Findex%2Ftype%2F4"
Signinheaders={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Length': '6637',
    'Content-Type': 'pplication/x-www-form-urlencoded',
    'Origin': Origin,
    'X-Requested-With': 'XMLHttpRequest',
    'Cache-Control':'max-age=0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'JSESSIONID=A3292ADC380256674E53DDC9ABCD24C6.cas55; _ga=GA1.3.549641581.1604386103; JWTUser=%7B%22account%22%3A%223190104963%22%2C%22id%22%3A427469%2C%22tenant_id%22%3A112%7D; _token=d0c07da3513106a67ef2eb3483db943a30a5f824f7cf0cc0841bad6102870352a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22_token%22%3Bi%3A1%3Bs%3A1021%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMzE5MDEwNDk2MyIsImNtY0dyb3VwQ29kZSI6IjE4MDAwMDA0NDgiLCJjbWNHcm91cElkIjoiZjE4YjhmNGVlNDBiY2QwNzY1Y2ZlOTg3Y2E4MjA0NmUiLCJlbWFpbCI6IjY2NjY2NjY2NkBxcS5jb20iLCJleHAiOjE2MDU4NTcxNTQsImxvZ2luVHlwZSI6ImRlZmF1bHQiLCJtcm9sZXMiOlt7ImNtY3JvbGUiOiIiLCJjb2RlIjoic3R1ZGVudCIsImNyZWF0ZWRfYXQiOiIyMDIwLTAyLTE5IDEzOjAwOjEyIiwiZGVzY3JpcHRpb24iOiLlrabnlJ8iLCJkaXNwbGF5X25hbWUiOiLlrabnlJ8iLCJpZCI6MjA1LCJpc2RlZmF1bHQiOiIwIn1dLCJtc3RydWN0dXJlcyI6W3siY29kZSI6IjAwMTAwMTAwMiIsImNyZWF0ZWRfYXQiOiIyMDIwLTExLTA1IDIxOjEzOjUxIiwiZGlzcGxheV9uYW1lIjoi5omA5pyJ55So5oi3IiwiaWQiOjU0NCwibGV2ZWwiOjIsInBhcmVudCI6eyJjb2RlIjoiMDAxIiwiY3JlYXRlZF9hdCI6IjIwMjAtMDItMTMgMTc6MTY6MzkiLCJkaXNwbGF5X25hbWUiOiLmtZnmsZ_lpKflraYiLCJpZCI6NTQxLCJsZXZlbCI6MSwicGNvZGUiOiIiLCJwaWQiOjB9LCJwY29kZSI6IiIsInBpZCI6NTQxfV0sInBhc3N3b3JkIjoiMDMxZjk0ODg5MGMyYzY1NjZiN2UwOTk5MDBhZjYzN2UiLCJwaG9uZSI6IjEzNjEwMDAwMTU1IiwicmVhbG5hbWUiOiLku7vkv4rlrociLCJzdWIiOjQyNzQ2OSwidGVuYW50X2lkIjoxMTJ9.yi6MwwLDLqt42dX3jBWPHfkveBXNaDP90d_t8OH3RW4%22%3B%7D; _pf0=b06AwPsupzAerTaileatjNRrza3%2Fi5GrmlTWULRqqe0%3D; _pc0=D6pQppquhujDEEGHfa86bQz7l0IKj5N0%2BQga7Y96w478OnWKeLdXILok09gUC4mh; _csrf=S8mwplVi9KWoF2WQ0TlCeEmtpRLjO%2Bsi%2F4yyLGgYSRw%3D; _pv0=3z1c42t2LcGzLcX2DZq6bzTjuTWTN3RqFTbtB2JIAi3zsYWt9hnKQZsFescapXlSBTYQQDiZND6C0X9qAVbrIwOYfw%2F812ldaK8pMmpblbwru0Q951bRmy8W0DPE%2FVrxF6AmYVqEHhkfh%2FmHZrGJtEOOyGaVsYDj1tznMtl67FDEJud3v%2BDairdQ1A43pwglMaubYjX0s9lDmaecJO0MlE0n6Jngr9AwY1mtnHD0soqvKzlBx7ZCF%2FmVbKoMxvhNCf7rGwzNvvnkPA1imPMEWTJDbLjxqFjzgJ14DCdH7IVhcx7vsmoH5urR9sOEsHcL%2B%2FF5jtjUwMlM4XIsHrXeXMbSudFt%2FwsQ%2BYg5scYV5g3s8DfLewWsT4UEowH2iwAHMCSOw0u42f5FUhg377DOcl70AtDWnlY1AD%2BaqhLL2LI%3D',
    'Accept-Encoding':Accept_Encoding,
    'Accept-Language': Accept_Language,
    'Connection':Connection,
    'Host': 'zjuam.zju.edu.cn',
    'Referer': 'https://zjuam.zju.edu.cn/cas/login?service=http%3A%2F%2F10.203.97.155%2Fcas%2Findex.php%3Fcallback%3Dhttp%3A%2F%2F10.203.97.155%2Fhome%2Fbook%2Findex%2Ftype%2F4',
    'User-Agent':User_Agent,
    'Origin':'https://zjuam.zju.edu.cn'
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

def get_code():

    APIget=requests.get(APIurl,headers=APIheaders)
    valpng=open("Function/valcode.png","wb")
    valpng.write(APIget.content)
    valpng.close()

    image = Image.open('Function/valcode.png')
    image = clear_image(image)
    #转化为灰度图
    imgry = image.convert('L')
    code = pytesseract.image_to_string(imgry,lang="num")
    os.remove('Function/valcode.png')
    code=re.findall("\d",code)
    if len(code)==4:return code[0]+code[1]+code[2]+code[3]
    else :return get_code()

def signin_old(userid,password):
    
    Signindata={
        'username': userid,
        'password': hashlib.md5(password.encode('utf8')).hexdigest(),
        'verify': get_code()
    }
    params={
        'service': 'http://10.203.97.155/cas/index.php?callback=http://10.203.97.155/home/book/index/type/4'
    }
    Signinpost=requests.post(Signinurl,headers=Signinheaders,params=params,data=Signindata)
    if Signinpost.json()["msg"]=="用户名或密码错误":
        print("userid or password false,please check:")
        userid=input(userid+"\n")
        password=input(password+"\n")
        return signin(userid,password)
    elif Signinpost.json()["msg"]=="验证码错误，请重新输入":
        return signin(userid,password)
    cookie=Signinpost.headers["Set-Cookie"]
    cookie=re.findall("=[^/]*;",cookie)
    for i in range(len(cookie)):
        cookie[i]=cookie[i][1:len(cookie[i])-1]
    return cookie

def signin(userid,password):
    
    Signindata={
        'username': 'userid',
        'password': '0c89bcab76f357bcadbb275ad026dd0b660c46380f2d599817b73d1ab5ad5a367278cabaa2faa8acd7362174e806e44d86fefb4b7a561ff6ce650d27fb1d2950',
        'authcode': '',
        'execution': '9186d309-dfc7-46f7-8880-3aa9de864c4b_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuUWxCNFpXOHhUbmRUUkZKc09WUkZSR2xFVGpVd1ZqbHRTVTlvU1daUVRubGphemREU0ROdlNITXlOVFp4YlcwdlpHNVpkVXBXYUdaSFFqSllSbFV5Y2pWaWNWcDZNWFpNUldoMWMyMW1kMGhCTW5WalpFNVpWa05STVdoa2RrMURNMDExV25kVmJUVm5aRlZQTWl0M1V6VTFVMDFPT0c5dU1teG5XRkF5UlRoa1VERndTa0ZMTkhwUlYydFFRemwyVUdOQ01UQmlkMGM1YlU0MlVtbHBZbm92TTNOaGEwVTJlRVZQUzJsdk5ETkhNMnBKVDFkVFF6SldhWEpDY25KWk1sUjVVVzR4YVVjelJVNWpUSEZuYmk5V04yNXZkaTh2ZEUxMWJFTktZVEJTTmpsUGQwZEJaRzF2WldwUVNHZGhTbFo0VEdwNk5EQkdNVE12TVRnemJYSTNMMGhUUVVsc1R6TnBLMGxMY2pWbGVsWTRiMlpvUW1wWEszcEJNbmxNZUhkM1VGQnNRVnAwZVN0a1JrY3phV2MxTUdwcVdVZFNhVlZKT0UxbVdYcG1kRGRNYlhSU05ERTNlVTVGYkZkNmJWQkZURE5SVEZwb1IwbE1NMWwzUzAxS1YxZ3ZSRGxEVGsxWlpqQTFSbVpwYTFCdVNXSmthREpCVFhsdE4wZFhZekp4YlhGV2FHVk9UVXRGYTJsT2FuRlpkWEpGUVRFM2VUZG1ORmxtZG5saVlUTm9LekJ1WWtndlUzQkJVbWhDWTNCRVFVRnZRVnBFTDJWRk5VaENNMDFMYm5KNmMwRk1VelJzYUdOV2F6WnZTbXd2ZERWaGRHaDBZbUl6Y1haUU9WbDFNalJIYURaaloxWkJjVTVMVDBKMlZGUlFjSHBHVVRaa2FTOU5WR2hwY1hGWWFWUlpiWGQzUmpSeWFYZGpValI1YTJkWlNrUjNaRGxLVmxCTWQxQnFka3c1WVhOaVQwOXFiVlIzVUZGUVNERjVPRkZJZFVoQ1MySk9RMEl6T1RJMU5EQmpUMlp3V21WMU5rVlBibXRHZDA5dlRUSkROVlp4VlU1YWNUQk9VbU5uV20xWVRteG5PR1J2UjBWVlFrVlpTM1pDYm0xb2MySm5ia2RUTm1JMGRsaGtTRTA1VmpCRk1HeFFNbTFxYkdvM1VHUXpTV3AyVWxkWGIwMXhaM015YWxsSFVrOXZkMGRwU1ZSWWFHWjFkMm8zTDNGMmRHNXZWV0YzWmsxbVpIWjVNSGhTVFRKTk1VVm1VSFoxWmxFeVZWZElRVzVMZURObVZVdG5OSHBxZEV0NlFrbGhRWE5YYmtwVFYzSnZWVU5VU1RWblZGazBPV016ZDBJM2NVaEtjMjgzYVdsSmVWcHZVMVpZWkRoRFQyRXZURTltSzJKUlZ6ZFBkRGRVY0hCTVdFRnBiMHBwTURKWVUzaGlaRFJWV1ZGUk1IWk5RMEZXZFRNdlRrRjFZVzAxWVc5Tk0wMVlibWQ2VmsxMlFscEdMMjE0YXpRMmFUSmxjbEo0TmpBM2JUZG1ZbUUwTDFoeE5uUTVNVkI1VkhscGFqTldNMmhSTkUxNVNWWkJiaXRFVWxsVldYSjNOVVF5Y3pWUlFtTnRXalo1UjB3M2JESTFMMDFaY1doeVRsZ3lRMDltYWsxWU0wWm5WblYzZUZsMmRXUlpjRGc1UzIwMlZFSmtVRGR4VFdwME5UZFZiVkZQTkhkWGJXZG5jRmt5T1hkcU9EaFFVblZ2TUM5VlYyTkdXVXhUVmtsRGEwNTBZemR5YzNOV1ZEQkpjbmszZVhoTGFIQTFaVEoyVVVSaFdtcFhkRmxWVVRCbFVYTjNOSGh3WVhsalVGTlFkR2RtUTNWSVlqUkxRM294ZDNoMmVXdFFTMjFWUW5WaldXY3ZZakpuVXk4NFpXeDFTbGhhUkVsaWExTjZTM1ZSYVRWNFYzRlZVaXRHVG5veWMyZDNaV3N5TUZWdWJDOVpSVmhxVTFwV2RUQktSMWRxWVZjeFVYbGlUWHA1THpoTlRGb3JSMjlLZWpFclUwZEJUVTkyYlZCV1MwNTFZV0ZUZG5oelRYQlJRemxwVGpoNVNHbFNSVmM0Ym5sRVJuZGFhRkpYYXk5U1ZYTkVUVVZpYjJKR1ZYTlFXVmg0YlhOUFpqQkZSbVp4V1hGNlNtSlVkbkpoWmxweVNISnhhRVo2VFdOMGFsSjZVM0JZSzA1eVpFMWhORWxvVDBOTGVsbDFUVU5HTkVvd09VWTJVbmcyUlU0dmN6ZE9UekpFUlROaVExSnRiR3haYzJVdk1YVmxiV05tVmpORVVVbHBRVVpET1c1VWREaGxRazAwUVZacGJ6QnhLMDlMYjJ4dFZteHpPSGRWZW0xSFdreEJXa1pwY2tWNVRtVktSa2xzUTBrNVExQkRhRnBFTlVaNFVuWnFNbk52U2xsMVpXRjROMDVwU3pkdVVFWlNkWFJ2UkZKNFFUWTNPRVpaWm14YVNWRm5jRlF3UTFnek1VY3lUMk5ZY1ZJeFNVWTFRMUZzVFZodFNHOUlWMXByTUU1alQyTkNaelZ5Yld4UGFUVTROblZpY0dkRlpqaEhXR1ZTYVRFeVNuZFNUa2xaUzB0VWFqSlphVk5HZWk5MlpUUkpOVEZWU25rd1RFdFdTVFUzUTFCM2JtdE1lbUl2UzBSblRXeEVkRFJaSzFkTFRVSjNWbGxTY0doUlNIUlBXbkJDZGxocE1sVTJORVp3T0RObU1XUk1PWGN5ZUhOMlNVdHFhRlZ5VTNGV1NHWkdiMnB3UTNZM1FsaDFhMGxVWjJSV2JESm9kR05WTXpsNWNtMDFjMXB4UW1aRFEyRkNUMnRKZVZOWFZUY3ZiU3RxVTFjNWVFeDJValI0Y0dsQlpuUjJTVzQxY25aWVZIaE9SakZUVEUxT2JIZzFXblpCUVRnMVJXSmFkMVp0WmxWSFIyWnFPRzF2T0RreVVFUmxiMGRLZFhwS2VISnRXVWh6WTJRMFFXcE1Ta1ZQYkV0VVdGVkNZMlpKT0hwVlZHdHNVekZVYUc1V0wwZGxVV0pRUlVkcGJDdGlTa1pZWlc1SWRqaG1ZbFF5ZGtkWVdIaEROWGgxYWxOT00zRlZSR0poT0dJMVJ6UjRTbWh4YTNCcUwwbEVWamN3VVdaQ1JEUlZRamx4TkZod1lrY3lkMUUxWjBsS05ubElhREJqTW5aQmRtNDJWbmxQY0dFclJGa3dPVkpGU1VaeWMyWlZPREJzWkZCS2JEUTVVRE5vVlVoRmJtWXZWbk5rV2tsM1N6UnZiVkJQZHl0bk5teENRa0pxUTB4QlFrbDZaRkY0TkhaVlpqWXZhVVpMVlVGaGRtdG9RMGhTTVhGVVYxVjZUekJUTjBSNFVERm5NbVZMY0ZaeWIwNUZTMU5FVEZaUWNHVnhZV3NyVDFsRGRWWlBOSGRJZEZCNVdtWlRiUzlHYjNsS2RqUXdSWG81U205RFdIQndaa293ZDFKSVdYZHNZVk5KZGtsWmRqQm9SVnBxVkRseldWcGFNSGRJUVRsU0swdEZOVWxPTmxRck9EVndZVWhxVkRFM1lWUlVRVm8xTW14dWJuRkdjbU5uT0U1NFdVRjVTRkJtVUU5MVJXZFFZMmxMZDBkUFFWWlhNM0l6ZGxCak5VVnNaMHd6ZVRSSE5tUm5VMlU1WnpKWlRGZFZLMFZIYTNCNGRYZHZXazFvU2tVdlYyNXBRMUF3VkZWcVNXcFFjMVIxTVRaT2NFMWtZVVZKYVZFdlMxcFFRakpaZVM5b1dHbzJiSEY1ZW5aalJrMW9VM0ZxUzBoME1uZHdWRVpVZVZGbVQzUlZjMlZsYlZRemFHTTJWek0zTnl0amVFZzNNR1JrZW5sUmFuVkNTMmxzY1ZwM1JUQkJhQ3RRTVVacVVsUTVlbUZhY0ZGNmVVVjNkell5ZVZNdlNWZ3JaM05CZEZoM1FqWklLMk5QZVdSMEt6bFVlSFV6YzBSV1kyUnlSRE56VFhkalowdFVVVWROYVd0T1V5OVRVMXBrUmtoclYyMXdUWE5HYlRCbmQzSkxNVzFMU0dwU1ZGRnZXakJzUmpWbU5TdG1URlpSZG1kNE0wMVRWbWRNVWtwWmRrcGtjRVpUVFRSemRVcGFRbFpHYjJoc2NrbHFXVFZFTVhkU2EweDRWbEIxVEZrd2RHaE5XWEZzSzFWV01IUk5TV2RETlZKWU9GTXpia1J4TTFkcmRtUXpXbTF5UlhCTlVFOWxPV2xOY1hoeVdVOVBSbU14YW5GVU4yWmFjblk1VmtaMGNrdHdOa3RaSzFCSU5rOURRMFJ6TVRZMGNrRlRPRUZLZGxvcmRXeFBjbFkzUVhoUldsaExhRXh6ZURka2FVOUtZVWRZUlRoUk1VZ3hUWGswU2pCa1FTOXJUMkpHT1dSRlF6TnNNR2x1TUZaQlQxZDZRelJZUTI4MFJGZ3lla0p6UjBkcVN6bFNkWEpKTkdkYWVUaHpWRGNyV1RWYWIzSmlhblpvVnpkalIzaFBZbFpxZW5KTE9IRlBMM1JqWldseGFsUlVWamM0VmpNMlNVOUlRek5aWlVaUEwyNXlVM2xUVm5KUk9WcFFTemRUVUcxTlEyeEhWRVowU0RsNWNXUjZiVFpvZERCeE5WbHlibEZhVFV4UVIwRXhiWHA0UlU5NU1GaGpOa3c0TkhwRVdFVnZVR1pzTUVvNVRXUmxjbWhzYUdaSU1GVXpTMHBLT1VOT1VUVnBaR3AyYzFaR2NFOVRjbXRXU1drNFdrbEZZVVUxVUhCaVpUVmhiblp5YkhreFpFcHhPR0pXV2twS2FHcGpMM2RHZVZkcGRVTjZWRWRGTVV0VkwwRm5TR3ByTTNwU1dFWTBSV0ZhZFU1blMzZFFabGhQYW1KNlRqZFlVMXBCYlZSRFoyMUZPQzl4ZEZsbVNYWnZRMVJxTUVwaVFtMXNkVWxaVUhkNlNtWlNlbWhJV21KalJHTjBlR2RKT1VOSlIzZFVXa3d6V25waVYzTjRjRlJPVEM4NVltRjRaSHB3YTJZclVIaE1VelJvUzNWRlZGcDZLM2xzYldSS2RHaDNZbTl3VGxneGJrTjNXbkJ2VXpSWFkyWTJUR2w1WTFFelNTdFpZeXMxYUd4clpHTklWalpET1VONlRWUnFNMlZVYm5aSU9WUkJUMVJCVkdWWFFXRndSa3ByUm01RE1Ua3hhRkJIYVcxbWNUaFBhbEExYzA5WlNFNUNjMXBqVUhwalJXNVZNV3N5S3k5NVdVVXJMMjV4UkhGdWFYTTFORkJpU2xsbU1ERTJaWG81YVdvcmJrNW9OMGRMT1RCQ2VrazRhMEZ4UjBsU1kwRkhVMnRqYjNwb1RIQm5SRm80VHk4NVYwZG1abFZ1T0hwcGVsaHJUVW9yUWxobWJWaDNja3gwVnpGWWVqaEdVSEF4VjJ0SmRUWlpTREJOVjBOTlpUZHlRVVIwZG05eFlXeEpObUpDTjJ0cFpEaG9Wak52ZHpCTE5UQnFUM2RqYTJacFJXRk5XSG96VDNvNVMwOTRkVmhGYW5sRWJYZElUMXBIZDFsMWFYVklabmM1ZG1rMVVHaHRMMDVpVjFSVmVEbFpPVU5xUzBWaGFYbE9iWGgzUVVoRVR6SkxVUzlJY0V4dmJFZG5jMjFvTVZCelZtRTFUSHB3TUhKT1lrcHZhRkEwWTA1UFMycFZWWEpPTUhKUFRtOWxSRXhHVVU1WVJEa3JZMk5OTkM4dlpFRkpkRUZvZW1vMFluaDFUV2xtWlUxelVsWmhjV05WYUdVM2RXUlJlRWx3WlRobE9HNWFlRkF3UzJSemMzbERSMHBqVmtGQ1ptdHpkM0puUVZRNGRWQm5PRzlTTm1ac1VGbGFhbE5HT0dac1RYaEVWbEZLTVVZNVFtTkVRVE0zY0VoaVVFZHpVSFEyVUhjMkx6UnNUVkJUWTJoYVpsRkxPSFZXWkdzM2NFMHljVTl1UzA5b01tRkdjU3Q1Vmxadk5IY3ZUalV2YjBsdlVqVlBUVXBHVlVSaGRIQXhlR2hDWkd4T1dWVTFSSEo1VEdSYVJtVXJWRFZvYTFFemN6VktSRkpFTUhac1pFOVJWRmh6Wm5SelZtZDNlVkZGWVhOa01GWTViRVpMWVhSWFNtRXhOSEptVlhZME9IaExVbXhtVERKVWRFMHJhbVZrSzBKWk5WVnNVbEk0ZERCWFdpdDFkRWw2TUd0NU0wTkVTVTVKV0EuY3Zwa1A4MDhXZXA0NGdQdEJmS3h0NE9tRWNrRjYwVDdWQXRROGhFYlFCd2RJQ2gzbE13RXdaSElWVEs0eDZVeG12R1h1U3VQZXJaWW1DRWUtZkt3eGc=',
        '_eventId': 'submit'
    }
    Signinpost=requests.post(Signinurl,headers=Signinheaders,data=Signindata)
    print(Signinpost.text)
'''
    if Signinpost.json()["msg"]=="用户名或密码错误":
        print("userid or password false,please check:")
        userid=input(userid+"\n")
        password=input(password+"\n")
        return signin(userid,password)
    elif Signinpost.json()["msg"]=="验证码错误，请重新输入":
        return signin(userid,password)
    cookie=Signinpost.headers["Set-Cookie"]
    cookie=re.findall("=[^/]*;",cookie)
    for i in range(len(cookie)):
        cookie[i]=cookie[i][1:len(cookie[i])-1]
    return cookie
'''
def orderday(mode):

    #cookie=signin(stuid,mmcode)
    orderheaders={
        'Accept': '*/*',
        'Cookie': 'redirect_url=%2Fbook%2Fnotice%2Fact_id%2F1612%2Ftype%2F4%2Flib%2F11; PHPSESSID=ST-7499419-CdbJGnt90ZvNg6XzERmx-zjueducn; userid=3190104963; user_name=%E4%BB%BB%E4%BF%8A%E5%AE%87; access_token=49d773a7e355419d1a0d760a3b40d934; expire=2020-11-30+20%3A05%3A53',
        'X-Requested-With': 'XMLHttpRequest',

        'Referer': Referer2,
        'Accept-Encoding':Accept_Encoding,
        'Accept-Language': Accept_Language,
        'Connection':Connection,
        'Host': Host,
        'Referer': Referer2,
        'User-Agent':User_Agent
    }

    start=datetime.datetime(2020,10,29)#1580 - 10.29
    now=list(time.localtime())
    end=datetime.datetime(now[0],now[1],now[2])
    day=1580+(end-start).days+(mode==1)
    data={
        'mobile': mobile,
        'id': day
    }

    orderurl='http://10.203.97.155/api.php/activities/%d/application2?mobile=%s&id=%d'%(day,mobile,day)
    cancelurl='http://10.203.97.155/api.php/activities/%d/quit'%day
    trytime=0
    if mode==2:
        while 1:
            orderget=requests.get(orderurl,headers=orderheaders,data=data)
            if orderget.json()["status"]==1:
                if day-1580==(end-start).days:print("当天已预约成功!")
                else :print("明天已预约成功")
                break
            time.sleep(0.5)
            trytime+=0.5
            print("%.1fs:Waiting for empty seat."%trytime)
    elif mode==3:
        cancelget=requests.get(cancelurl,headers=orderheaders)
        if cancelget.json()["status"]==1 or cancelget.json()["msg"]=="取消成功":
            print("当天已取消成功")
    else:
        while 1:
            orderget=requests.get(orderurl,headers=orderheaders,data=data)
            if orderget.json()["status"]==1 or orderget.json()["msg"]=="活动申请失败，已申请的活动时间冲突！":
                if day-1580==(end-start).days:print("当天已预约成功!")
                else :print("明天已预约成功")
                break
            print(orderget.json())
            time.sleep(0.5)
            trytime+=0.5
            print("%.1fs:Waiting for empty seat."%trytime)

if __name__=="__main__":
    mode=3
    if mode==1:
        print(hashlib.md5(mmcode.encode('utf8')).hexdigest())
    elif mode==2:
        signin(stuid,mmcode)
    elif mode==3:
        orderday(int(input("0 for today & 1 for tomorrow & 2 for meal & 3 for quit\n")))
    elif mode==4:
        APIget=requests.get(APIurl,headers=APIheaders)
        valpng=open("Function/valcode/0.png","wb")
        valpng.write(APIget.content)
        valpng.close()