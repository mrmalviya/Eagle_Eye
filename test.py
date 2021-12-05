import subprocess
import os

while True:
	multiple_target_ip=input("Enter Target IPs [E.g 10.10.10.20,10.10.10.30]\t")
	print("\n\n")
	subprocess.call(["nmap",multiple_target_ip])
	print("\n\n")
