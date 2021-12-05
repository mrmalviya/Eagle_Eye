import os
import time
import subprocess

def whois_lookup():
	user_ip = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
	os.system("reset")
	print("\033[34m[~] Searching using Whois Lookup: \033[0m".format(user_ip) + user_ip)
	time.sleep(0.2)
	print(subprocess.call(["whois",user_ip]))
	
