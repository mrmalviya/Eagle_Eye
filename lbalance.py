import os
import subprocess
import time

def load_balancer():
	try:
		user_input = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
		os.system("reset")
		print("\033[34m[~] Searching for Load Balancer : \033[0m".format(user_input) + user_input)
		time.sleep(0.5)
		subprocess.call(["lbd",user_input])
	except Exception:
		pass

load_balancer()
