import subprocess

def dirb():
	website=input("\033[1;36;40m[+] Enter Website Name : \033[1;m")
	subprocess.call(["dirb",website])
