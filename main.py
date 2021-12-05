#!/usr/bin/env/python3

# ++++++++++++++++++++++++++++++++++++++++++++++
# GitHub: https://github.com/mrmalviya
# Instagtam : __firewall
# Author: Mr. Malviya 
# ++++++++++++++++++++++++++++++++++++++++++++++



import optparse
import subprocess
import re
import host_scan as hs
import hydra as h
import crunch as c
import whois as w
import dns as d
import tr as t
import sys
import os
import banner as b
import locator as l
import dirb as dr

def print_sub():
		#os.system("clear")
		user_input_main="-1"
		print("\033[1;32;40m[+] [1] Most Popular Nmap Commands\033[1;m")
		print("\033[1;32;40m[+] [2] Crack password Using Hydra\033[1;m")
		print("\033[1;32;40m[+] [3] Generate wordlist Using Crunch\033[1;m")
		print("\033[1;32;40m[+] [4] Whois Lookup\033[1;m")
		print("\033[1;32;40m[+] [5] DNS Lookup\033[1;m")
		print("\033[1;32;40m[+] [6] IP Locator\033[1;m")
		print("\033[1;32;40m[+] [7] Traceroute\033[1;m")
		print("\033[1;32;40m[+] [8] Scan WebSite Directory\033[1;m")
		print("\033[0;32;40m[+] [00] EXIT")
		print("\n")
		user_input_main=input(" =>  ")
		
		if user_input_main=="1":
			try:
				nmap_object=nmap_class()
				nmap_object.select_option()
			except:
				print("\033[1;31;40m\t\t[-] Failed To Run NMAP Skipping Step.")
				pass
		elif user_input_main=="2":
			try:
				hydra_object=hydra_class()
				hydra_object.hydra_option()
			except:
				print("\033[1;31;40m\t\t[-] Failed To Run HYDRA Skipping Step.")
				pass
		elif user_input_main=="3":
			try:
				crunch_object=crunch_class()
				crunch_object.my_crunch()
			except:
				print("\033[1;31;40m\t\t[-] Failed To Run CRUNCH Skipping Step.")
				pass
		elif user_input_main=="4":
			try:
				whois_object=whois_class()
				whois_object.my_whois()
			except:
				print("\033[1;31;40m\t\t[-] Failed To Run WHOIS Skipping Step.")
				pass
		elif user_input_main=="5":
			try:
				dns_object=dns_class()
				dns_object.my_class()
			except:
				print("\033[1;31;40m\t\t[-] Failed To Run NMAP Skipping Step.")
				pass
		
		elif user_input_main=="6":
			try:
				locator_object=locator_class()
				locator_object.locator()
			except Exception:
				print("\033[1;31;40m\t\t[-] Failed To Run Locator Skipping Step.")
				pass
		elif user_input_main=="7":
			try:
				trace_route_object=trace()
				trace_route_object.traceroute_function()
			except Exception:
				print("\033[1;31;40m\t\t[-] Failed To Run Traceroute Skipping Step.")
				pass
		elif user_input_main=="8":
			try:
				dirb_object=dirb_class()
				dirb_object.dirb_function()
			except Exception:
				print("\033[1;31;40m\t\t[-] Failed To Run Traceroute Skipping Step.")
				pass
			
		elif user_input_main=="00":
			try:
				print("\033[1;31;40mBye Bye ! ! !")
				sys.exit(0)
			except:
				print("\033[1;31;40m\t\t[-] Failed To Exit !!! Really ")
				pass	
		else:
			print("\n\033[1;31;40m[-]Wrong Input\033[1;m\n")
			os.system("reset")
		print_sub()
		
		
class nmap_class:
	ip_address="127.0.0.1"
	port=""
		
	def select_option(self):
		
		user_input=-1
		print("\n\033[1;36;40m\t\t\t\t[+] [1] Scan a single target\n\t\t\t\t[+] [2] Scan multiple targets\033[1;m")
		print("\033[1;36;40m\t\t\t\t[+] [3] Scan a list of targets\n\t\t\t\t[+] [4] Scan a range of hosts\033[1;m")
		print("\033[1;36;40m\t\t\t\t[+] [5] Scan an entire subnet \n\t\t\t\t[+] [6] Scan random hosts\033[1;m")
		print("\033[1;36;40m\t\t\t\t[+] [7] Perform an aggressive scan\n\t\t\t\t[+] [8] Scan an IPv6 target \n\033[1;m")
		print("\033[1;36;40m\t\t\t\t[+] [00] Main Menu\n\033[1;m")
	
		user_input=int(input("=> "))
		
		
		if user_input==1:
				os.system("reset")
				hs.single_target()

		elif user_input==2:
				os.system("reset")
				hs.multiple_target()
			
		elif user_input==3:
			
				os.system("reset")
				hs.list_of_target()
		
		elif user_input==4:
		
				os.system("reset")
				hs.range_of_host()
		
		elif user_input==5:
	
				os.system("reset")
				hs.range_of_host()
	
		elif user_input==6:
				os.system("reset")
				hs.random_host()

		elif user_input==7:
			
				os.system("reset")
				hs.aggresive_scan()
		elif user_input==8:
				os.system("reset")
				hs.ipvsix_scan()
		elif user_input==00:
				os.system("reset")
				print_sub()
		else:
			print("\n\033[1;31;40m[-]Wrong Input\n")
			os.system('clear')
		self.select_option()
		
		
class hydra_class:
	
	def hydra_option(self):
		os.system("reset")
		
		print("Select target protocol :\n")
		user_input=int(input("\n\033[1;36;40m\t\t\t\t[+] [1]SSH\n\t\t\t\t[+] [2]MYSQL\n\t\t\t\t[+] [3]SMB\n\t\t\t\t[+] [4]FTP\n\t\t\t\t[+] [5]HTTP\n\t\t\t\t[+] [6] MAIN MENU\033[1;m"))
		if user_input==1:
			try:
				h.ssh()
			except Exception:
				pass
		elif user_input==2:
			try:
				h.mysql()
			except Exception:
				pass
		elif user_input==3:
			try:
				h.smb()
			except Exception:
				pass
		elif user_input==4:
			try:
				h.ftp()
			except Exception:
				pass
		elif user_input==5:
			try:
				h.http_post()
			except Exception:
				pass
		elif user_input==6:
			print_sub()
		else:
			print("\nWrong Input\n")
		self.hydra_option()
	
	
class crunch_class:
	
	def my_crunch(self):
		print("\033[1;36;40m\t\t\t\t[+] [1] Generating wordlist without using the character string\n\033[1;36;40m\t\t\t\t[+] [2] Generating wordlist using the character string\033[1;m")
		print("\033[1;36;40m\t\t\t\t[+] [3] Generating wordlist with pattern\n\033[1;36;40m\t\t\t\t[+] [4] Generate wordlist with Duplicate character limit \033[1;m\n")
		input_menu=int(input(""))
		
		if input_menu==1:
			try:
				c.without_char()
			except Exception:
				pass
		elif input_menu==2:
			try:
				c.with_char()
			except Exception:
				pass
		elif input_menu==3:
			try:
				c.with_pattern()
			except Exception:
				pass
		elif input_menu==4:
			try:
				c.permutation()
			except Exception:
				pass
		else:
			print("Invalid Input")
			
		self.my_crunch()

	#print(print_sub_2.__doc__)
	
	
class whois_class:
	def my_whois(self):
		w.whois_lookup()
		
		

class dns_class:
	def my_class(self):
		d.dns_lookup()

class locator_class:
	def locator(self):
		l.ip_finder()



class trace:
	def traceroute_function(self):
		t.trace_route()
		
class dirb_class:
	def dirb_function(self):
		dr.dirb()


os.system("reset")
b.banner_one()
print_sub()
