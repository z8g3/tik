#MPro
import requests
from user_agent import generate_user_agent
from colorama import Fore
import sys as mp
import time as mpp
def slow(mpr):
	for mppp in mpr + "\n":
		mp.stdout.write(mppp)
		mp.stdout.flush()
		mpp.sleep(0.5 / 120)
slow(f"{Fore.RED}\n𝙼𝚘𝚑𝚊𝚖𝚖𝚎𝚍𝙿𝚛𝚘\nTelegram >> 	@xx6gs\nMy Channel >> @xx4gs\nInstagram >> @xx4gs{Fore.WHITE}\n")
list=input(f"{Fore.RED}Name list user >> {Fore.WHITE}")
tokne= input(f"{Fore.RED} Tokne Tele >> {Fore.WHITE}")
id= input(f"{Fore.RED} Id Tele >> {Fore.WHITE}")
list1= open(list, 'r')
def mpro_user():
	while True:
		list2=list1.readline().split('\n')[0]
		url=f'https://www.tiktok.com/@{list2}'
		head={
			'User-Agent': generate_user_agent(),
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		}
		rq = requests.get(url, headers=head).status_code
		if rq == 200:
			print(f"{Fore.RED} user Found >> {list2}{Fore.WHITE}")
		elif rq == 404:
			print(f"{Fore.BLUE} user Not Found >> {list2}{Fore.WHITE}")
			tlg =(f'https://api.telegram.org/bot{tokne}/sendMessage?chat_id={id}&text= 𝚞𝚜𝚎𝚛 𝚃𝚒𝚔𝚝𝚘𝚔✅>> {list2}\n\n	 𝙼𝚘𝚑𝚊𝚖𝚖𝚎𝚍𝙿𝚛𝚘 >> 𝚃𝚎𝚕𝚎:@xx4gs')
			reqTele = requests.post(tlg)
mpro_user()
