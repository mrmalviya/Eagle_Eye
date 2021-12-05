import subprocess
import time
import os

def trace_route():
	input_url = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
	os.system("reset")
	print("\033[34m[~] Searching . . .\033[0m".format(input_url) + input_url)
	time.sleep(0.2)
	subprocess.call(["traceroute",input_url])


