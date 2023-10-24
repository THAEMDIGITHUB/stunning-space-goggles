try:import requests
except:import os;os.system('pip install requests')
from datetime import datetime
import requests,random,os,sys
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from time import sleep,strftime
try:from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:os.system('pip install pystyle'); from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
pinkx='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
den='[1;90m'
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\e[35m'
hong='[1;95m'
thanh_xau=trang+'~'+red+'['+vang+'⟨⟩'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'✓'+red+'] '+trang+'➩ '+luc
def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1',53))
        return True
    except OSError:
        pass
    return False
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
banners=f"""██████╗░██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██║░░██║██║░░░██║██╔══██╗
██████╔╝███████║██║░░░██║██║░░╚═╝
██╔═══╝░██╔══██║██║░░░██║██║░░██╗
██║░░░░░██║░░██║╚██████╔╝╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░"""
thongtin=f"""{thanh_xau}{vang}Verison 3.3.2 Dsing By Lê Hoàng Phúc{end}"""     

def lehoangphuc(so):
	a='[1;95m────'*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.003)
	print()
def banner():
	print('[0m',end='')
	os.system("clear")
	a=Colorate.Horizontal(Colors.yellow_to_red,banners)
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
	print()
	print(thongtin)

banner()
	

def nghingoi(delay):
	for x in range(delay,0,-1):
		print("\r\033[1;93m  ZYTH \033[1;91m ~>       \033[1;92m Z      \033[1;91m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;91m  ZYTH \033[1;91m   ~>     \033[1;92m ZY     \033[0;31m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;92m  ZYTH \033[1;91m     ~>   \033[1;92m ZYT    \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;94m  ZYTH \033[1;91m       ~> \033[1;92m ZYTH   \033[0;31m | "+str(x)+" | \r", end='')

		sleep(0.14)
	print("\r\r\033[1;95m    ZYTH                         \r", end='')
	sleep(0.1)

list_token_page=[]
list_id_page=[]
token_s=1
banner()
lehoangphuc(14)
print(f'{thanh_xau}{redz}[ENTER - DỪNG NHẬP]{end}')
while(True):
    token_fb=input(f'{thanh_xau}{luc}ACCESS_TOKEN FACEBOOK {token_s} :{vang} ')
    if token_fb=='' and len(list_token_page)>0:break
    id_page=input(f'{thanh_xau}{luc} PAGE ID {token_s} : {vang}')
    get_token_page=requests.get(f'https://graph.facebook.com/{id_page}?fields=access_token&access_token={token_fb}').json()
    if 'access_token' in get_token_page:
        token_page=get_token_page['access_token']
        list_token_page.append(token_page)
        list_id_page.append(id_page)
        token_s=token_s+1
    elif 'error' in get_token_page:print(get_token_page['error']['message'])
    else:print(get_token_page)
banner()
lehoangphuc(14)
choice=input(f'{thanh_xau}{luc}[ENTER - TỰ TÁCH] {trang}[BẤT KÌ - KHÔNG TỰ TÁCH]\n{thanh_xau}{luc}NHẬP LỰA CHỌN: {vang}')
while(True):
    try:delay=int(input(f'{thanh_xau}{luc}NHẬP DELAY: {vang}'));break
    
    except:print('[KZT][?]');sleep(0.5)
s=0
banner()
while(True):
	
    print(f'{thanh_xau}{redz} ĐANG TẠO PAGE{end}','          ',end='\r')
    for x in range(len(list_token_page)):
        try:
            token_page=list_token_page[x]
            id_page=list_id_page[x]
            latitude=random.randrange(9999)
            longitude=random.randrange(3333)
            store_number=random.randrange(999)
            #name='T O K E N'
            name=requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/female?count=2').json()['data'][0]['name']
            register=requests.post(f'https://graph.facebook.com/v12.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','always_open': 'false','differently_open_offerings': '{}','id': id_page,'ignore_warnings': 'true','is_franchise': 'false','locale': 'vi_VN','location': '{"city_id":2599270,"latitude":"21.'+str(latitude)+'","longitude":"105.2'+str(longitude)+'","street":"'+name+'","zip":"10000"}','method': 'post','permanently_closed': 'false','phone': '+84395581887','pickup_options': '[]','place_topics': '["123377808095874","530553733821238"]','pretty': '0','price_range': 'Unspecified','store_name': name,'store_number': store_number,'suppress_http_code': '1'}).json()
            if 'id' in register:
                s=s+1
                id_register=register['id']
                time=datetime.now().strftime("%H:%M:%S")
                if choice=='':
                    print(f'{thanh_xau}{lam}[{s}]{luc}[SUCCESSFULY ]{hong}[{time}]{trang}[{name.upper()}]{vang}[{id_register}]',end='\r')
                    tach=requests.post(f'https://graph.facebook.com/v12.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','locale': 'vi_VN','location_page_id': id_register,'method': 'delete','pretty': '0','store_number': store_number,'suppress_http_code': '1'}).json()
                    if 'success' in tach:print(f'{thanh_xau}{lam}[{s}]{luc}[SUCCESSFULY  + DELETED]{hong}[{time}]{trang}[{name.upper()}]{vang}[{id_register}]')
                else:print(f'{thanh_xau}{red}[{s}]{luc}[SUCCESSFULY ]{hong}[{time}]{trang}[{name.upper()}]{vang}[{id_register}]')
                
            elif 'error' in register:print(register['error']['message']);huykazuto_delay(0)
            else:print(register);huykazuto_delay(0)
        except:print('{thanh_xau}{luc}[NETWORK ERROR !]','          ',end='\r')
nghingoi(dl)