
import subprocess
import os

reason='--reason'
op="malviya.txt"



def single_target():
	''' This Scans a single IP
		Example: 192.168.1.1
	'''
	single_target_ip=input("\033[1;35;40mEnter Target IP [E.g 10.10.10.20] : \033[1;m")
	print("\n\n")
	subprocess.call(["nmap",single_target_ip,reason])
	print("\n\n")

	

def multiple_target():
	''' User Can Scan Multiple Targets
		Example: 192.168.1.1,192.168.1.2,192.168.1.3
	'''
	multiple_target_ip=input("\033[1;35;40mEnter Target IPs [E.g 10.10.10.20,10.10.10.30]\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",multiple_target_ip,reason])
	print("\n\n")

def list_of_target():
	''' This Will Scan Multiple Targets Located in Files
		Example: Place Location Of Files
	'''
	gen_var=input("\033[1;35;40mEnter Target IPs Location \n\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-iL",gen_var,reason])
	print("\n\n")

def range_of_host():
	''' This Scans Complete Range Of IPs
	'''
	gen_var=input("\033[1;35;40mEnter Target IP Range OR CIDR \n\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,reason])
	print("\n\n")


def random_host():
	''' Just Give Count Of Ip And It Will Scan Random Is
		Example: 2 {It Will Scan 2 Random IPs}
	'''
	gen_var=input("\033[1;35;40mEnter Number of IPs \n\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-iR",gen_var,reason])
	print("\n\n")

def aggresive_scan():
	''' It Runs Aggresive Scans
		Example: 192.168.1.1
	'''
	gen_var=input("\033[1;35;40mEnter Target IPs \n\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-A",gen_var,reason])
	print("\n\n")

def ipvsix_scan():
	''' This Option Will Scan IPv6 
		Example: FE80:CD00:0000:0CDE:1257:0000:211E:729C
	'''
	gen_var=input("\033[1;35;40mEnter Target IPv6 Address \n\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-6",gen_var,reason])
	print("\n\n")
	
	
def tcp_syn():
	''' This is another form of TCP scan. The difference is unlike a normal TCP scan, nmap itself crafts a syn packet, which is the first packet that is sent to establish a TCP connection. What is important to note here is that the connection is never formed, rather the responses to these specially crafted packets are analyzed by Nmap to produce scan results.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sS",gen_var,reason])
	print("\n\n")
	
def tcp_connect():
	'''
	A TCP scan is generally used to check and complete a three-way handshake between you and a chosen target system. A TCP scan is generally very noisy and can be detected with almost little to no effort. This is “noisy” because the services can log the sender IP address and might trigger Intrusion Detection Systems.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sT",gen_var,reason])
	print("\n\n")
	
	
def udp_scan():
	'''
	UDP scans are used to check whether there is any UDP port up and listening for incoming requests on the target machine. Unlike TCP, UDP has no mechanism to respond with a positive acknowledgment, so there is always a chance for a false positive in the scan results. However, UDP scans are used to reveal Trojan horses that might be running on UDP ports or even reveal hidden RPC services. This type of scan tends to be quite slow because machines, in general, tend to slow down their responses to this kind of traffic as a precautionary measure.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sU",gen_var,reason])
	print("\n\n")
	
def ack_scan():
	'''
	ACK scans are used to determine whether a particular port is filtered or not. This proves to be extremely helpful when trying to probe for firewalls and their existing set of rules. Simple packet filtering will allow established connections (packets with the ACK bit set), whereas a more sophisticated stateful firewall might not.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sA",gen_var,reason])
	print("\n\n")


def window_scan():
	'''
	Window scan is exactly the same as ACK scan except that it exploits an implementation detail of certain systems to differentiate open ports from closed ones, rather than always printing unfiltered when a RST is returned. It does this by examining the TCP Window value of the RST packets returned. On some systems, open ports use a positive window size (even for RST packets) while closed ones have a zero window. Window scan sends the same bare ACK probe as ACK scan
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sW",gen_var,reason])
	print("\n\n")

def mainmon_scan():
	'''
	The Maimon scan is named after its discoverer, Uriel Maimon. He described the technique in Phrack Magazine issue #49 (November 1996). Nmap, which included this technique, was released two issues later. This technique is exactly the same as NULL, FIN, and Xmas scan, except that the probe is FIN/ACK. According to RFC 793 (TCP), a RST packet should be generated in response to such a probe whether the port is open or closed. However, Uriel noticed that many BSD-derived systems simply drop the packet if the port is open.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sM",gen_var,reason])
	print("\n\n")
	
#++++++++++++++++++++++++++++++++++++++++HOST DISCOVERY+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

def listtarget_scan():
	'''
	No Scan. List targets only
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sL",gen_var,reason])
	print("\n\n")

def hostonly_scan():
	'''
	Disable port scanning. Host discovery only.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-sn",gen_var,reason])
	print("\n\n")

def portscan_scan():
	'''
	Disable host discovery. Port scan only.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-Pn",gen_var,reason])
	print("\n\n")

def arp_scan():
	'''
	One of the most common Nmap usage scenarios is to scan an ethernet LAN. On most LANs, especially those using private address ranges granted by RFC 1918, the vast majority of IP addresses are unused at any given time. When Nmap tries to send a raw IP packet such as an ICMP echo request, the operating system must determine the destination hardware (ARP) address corresponding to the target IP so that it can address the ethernet frame properly. This requires it to issue a series of ARP requests. This is shown in Example 3.11, where a ping scan is attempted against a local ethernet host. The --send-ip option tells Nmap to send IP level packets (rather than raw ethernet) even though it is a local network. Wireshark output of the three ARP requests and their timing has been pasted into the session.
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-PR",gen_var,reason])
	print("\n\n")

def nodns_scan():
	'''
	Host Discovery Without DNS resolution
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	
	subprocess.call(["nmap","-n",gen_var,reason])
	print("\n\n")

#+++++++++++++++++++++++++++++++++++++(Port Specification)++++++++++++++++++++++++++++++++++++++++++++++++++++



def nodns_scan():
	'''
	Scan specific port
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	port_var=input("\nProvide Port Number\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-p",port_var,reason])
	print("\n\n")
	
	
def range_of_port_scan():
	'''
	Scan Range of Port
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	port_var=input("\nProvide Port Number Eg. 21-100\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-p",port_var,reason])
	print("\n\n")
	
def all_port_scan():
	'''
	Scan all Port
	'''
	gen_var=input("Enter Target IP\t\033[1;m")
	#port_var=input("\nProvide Port Number Eg. 21-100\t")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-p-",reason])
	print("\n\n")
	
	

def service_port_scan():
	'''
	Port scan from service name
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	port_var=input("\nProvide Service Name Eg. http,https\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-p",port_var,reason])
	print("\n\n")
	
	
def fast_port_scan():
	'''
	Fast Port Scan (100 Ports)
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	#port_var=input("\nProvide Service Name Eg. http,https\t")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-F",reason])
	print("\n\n")


def top_port_scan():
	'''
	Port Scan. It Scan Top x Ports
	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	port_var=input("\nProvide Number of Port Eg. 25\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"--top-ports",port_var,reason])
	print("\n\n")


#+++++++++++++++++++++++++++++++++++++Service and Version Detection++++++++++++++++++++++++++++++++++++++++++

def version_service_scan():
	'''
	 Attempts to determine the version of the service running on port

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	#port_var=input("\nProvide Service Name Eg. http,https\t")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-sV",reason])
	print("\n\n")


def intensity_scan():
	'''
	 Intensity level 0 to 9. Higher number increases possibility of correctness

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	port_var=input("\nProvide Intensity Level\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-sV","--version-intensity",port_var,reason])
	print("\n\n")

def all_scan():
	'''
	 Enables OS detection, version detection, script scanning, and traceroute

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-A",reason])
	print("\n\n")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++OS Detection+++++++++++++++++++++++++++++++++++++++++++++



def tcp_os_scan():
	'''
	  Remote OS detection using TCP/IP stack fingerprinting

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-O",reason])
	print("\n\n")


def limit_os_scan():
	'''
	   If at least one open and one closed
	TCP port are not found it will not try
	OS detection against host


	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-O","--osscan-limit",reason])
	print("\n\n")

def limit_os_scan():
	'''
	   If at least one open and one closed
	TCP port are not found it will not try
	OS detection against host


	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-O","--osscan-limit",reason])
	print("\n\n")

#++++++++++++++++++++++++++++++++++++++++++++++++++NSE SCRIPT++++++++++++++++++++++++++++++++++++++++++++++++


def discovery_script():
	'''
	  Scan with default NSE scripts. Considered useful for discovery and safe

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-sC",reason])
	print("\n\n")


def site_map_script():
	'''
	  http site map generator

	'''
	gen_var=input("\033[1;35;40mEnter Target Website\t\033[1;m")
	gen_var="--script=http-sitemap-generator "+gen_var
	print("\n\n")
	subprocess.call(["nmap","-Pn",gen_var,reason])
	print("\n\n")
	
	
def sql_script():
	'''
	  Check for SQL injections

	'''
	gen_var=input("\033[1;35;40mEnter Target Website\t\033[1;m")
	gen_var="--script=http-sql-injection "+gen_var
	print("\n\n")
	subprocess.call(["nmap","-p80",gen_var,reason])
	print("\n\n")
	
	
def xss_script():
	'''
	Detect cross site scripting vulnerabilities

	'''
	gen_var=input("\033[1;35;40mEnter Target Website\t\033[1;m")
	gen_var="--script=http-unsafe-output-escaping "+gen_var
	print("\n\n")
	subprocess.call(["nmap","-p80",gen_var,reason])
	print("\n\n")
	
	
#++++++++++++++++++++++++++++++++++++++++++++++++++Firewall/IDS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def setmtu_script():
	'''
	Set your own offset size (MTU)

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	num_var=input("\n\033[1;35;40mSet Offset\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"--mtu",num_var,reason])
	print("\n\n")

def spoof_ip_script():
	'''
	 Send scans from spoofed IPs

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	num_var=input("\n\033[1;35;40mEnter Spoofed IPs eg. 192.168.1.101,192.168.1.102,192.168.1.103,192.168.1.23\t\033[1;m")
	print("\n\n")
	subprocess.call(["nmap","-D",num_var,gen_var,reason])
	print("\n\n")
	
	
	
def fragment_script():
	'''
	fragment packes for evading firewall

	'''
	gen_var=input("\033[1;35;40mEnter Target IP\t\033[1;m")
	#num_var=input("\nSet Offset\t")
	print("\n\n")
	subprocess.call(["nmap",gen_var,"-f",reason])
	print("\n\n")


#+++++++++++++++++++++++++


