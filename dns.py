import time
import subprocess
import os

def dns_lookup():
		user_input = input("\033[1;35;40m[+] Enter Domain or IP Address: \033[1;m").lower()
		os.system("reset")
		print("\033[34m[~] Searching for DNS Lookup: \033[0m".format(user_input) + user_input)
		time.sleep(0.5)
		subprocess.call(["dig",user_input,"trace","ANY"])

