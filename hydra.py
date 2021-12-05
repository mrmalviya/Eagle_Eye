import subprocess


def ssh():
	port="22"
	threading="4"
	ip="127.0.0.1"
	ip=input("Enter Ip Address : ")
	print("\n[1] Try single username and single password\n[2] Single username multiple password")
	print("\n[3] Multiple username multiple password\n[4] Multiple username single password\n")
	user_menu_input=input("")
	
	custom_port=input("Do you want to use custom port (22) ?(y or n)")
	if custom_port=="y":
		port_number=input("Enter custom SSH Port number: ")
		port=port_number
	else:
		print("Invalid selection using default port 22.")
		
	custom_thread=input("Do you want to change thread ? (y or n)(default=4)")
	if custom_thread=="y":
		th_count=input("Enter threading count : ")
		threading=th_count
		
	if user_menu_input==1:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-p",pass_name,ip,"-t",threading,"ssh","-s",port])
		print("\n\n")
		
	if user_menu_input==2:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-P",pass_name,ip,"-t",threading,"ssh","-s",port])
		print("\n\n")
	
	if user_menu_input==3:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-P",pass_name,ip,"-t",threading,"ssh","-s",port])
		print("\n\n")
		
		
	if user_menu_input==4:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-p",pass_name,ip,"-t",threading,"ssh","-s",port])
		print("\n\n")
		
	
	
	
	
def mysql():
	port="3306"
	threading="4"
	ip="127.0.0.1"
	ip=input("Enter Ip Address : ")
	print("\n[1] Try single username and single password\n[2] Single username multiple password")
	print("\n[3] Multiple username multiple password\n[4] Multiple username single password\n")
	user_menu_input=input("")
	
	custom_port=input("Do you want to use custom port (3306) ?(y or n)")
	if custom_port=="y":
		port_number=input("Enter custom MYSQL Port number: ")
		port=port_number
	else:
		print("Invalid selection. Using default port 3306.")
		
	custom_thread=input("Do you want to change thread ? (y or n)(default=4)")
	if custom_thread=="y":
		th_count=input("Enter threading count : ")
		threading=th_count
		
	if user_menu_input==1:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-p",pass_name,ip,"-t",threading,"mysql","-s",port])
		print("\n\n")
		
	if user_menu_input==2:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-P",pass_name,ip,"-t",threading,"mysql","-s",port])
		print("\n\n")
	
	if user_menu_input==3:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-P",pass_name,ip,"-t",threading,"mysql","-s",port])
		print("\n\n")
		
		
	if user_menu_input==4:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-p",pass_name,ip,"-t",threading,"mysql","-s",port])
		print("\n\n")



def smb():
	port="445"
	threading="4"
	ip="127.0.0.1"
	ip=input("Enter Ip Address : ")
	print("\n[1] Try single username and single password\n[2] Single username multiple password")
	print("\n[3] Multiple username multiple password\n[4] Multiple username single password\n")
	user_menu_input=input("")
	
	custom_port=input("Do you want to use custom port (445) ?(y or n)")
	if custom_port=="y":
		port_number=input("Enter custom smb Port number: ")
		port=port_number
	else:
		print("Invalid selection. Using default port 445.")
		
	custom_thread=input("Do you want to change thread ? (y or n)(default=4)")
	if custom_thread=="y":
		th_count=input("Enter threading count : ")
		threading=th_count
		
	if user_menu_input==1:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-p",pass_name,ip,"-t",threading,"smb","-s",port])
		print("\n\n")
		
	if user_menu_input==2:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-P",pass_name,ip,"-t",threading,"smb","-s",port])
		print("\n\n")
	
	if user_menu_input==3:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-P",pass_name,ip,"-t",threading,"smb","-s",port])
		print("\n\n")
		
		
	if user_menu_input==4:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-p",pass_name,ip,"-t",threading,"smb","-s",port])
		print("\n\n")


def ftp():
	port="21"
	threading="4"
	ip="127.0.0.1"
	ip=input("Enter Ip Address : ")
	print("\n[1] Try single username and single password\n[2] Single username multiple password")
	print("\n[3] Multiple username multiple password\n[4] Multiple username single password\n")
	user_menu_input=input("")
	
	custom_port=input("Do you want to use custom port (21) ?(y or n)")
	if custom_port=="y":
		port_number=input("Enter custom ftp Port number: ")
		port=port_number
	else:
		print("Invalid selection. Using default port 21.")
		
	custom_thread=input("Do you want to change thread ? (y or n)(default=4)")
	if custom_thread=="y":
		th_count=input("Enter threading count : ")
		threading=th_count
		
	if user_menu_input==1:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-p",pass_name,ip,"-t",threading,"ftp","-s",port])
		print("\n\n")
		
	if user_menu_input==2:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-P",pass_name,ip,"-t",threading,"ftp","-s",port])
		print("\n\n")
	
	if user_menu_input==3:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-P",pass_name,ip,"-t",threading,"ftp","-s",port])
		print("\n\n")
		
		
	if user_menu_input==4:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-p",pass_name,ip,"-t",threading,"ftp","-s",port])
		print("\n\n")


	
def http_post():
	port="80"
	threading="4"
	ip="127.0.0.1"
	ip=input("Enter Ip Address : ")
	print("\n[1] Try single username and single password\n[2] Single username multiple password")
	print("\n[3] Multiple username multiple password\n[4] Multiple username single password\n")
	user_menu_input=input("")
	
	custom_port=input("Do you want to use custom port (80) ?(y or n)")
	if custom_port=="y":
		port_number=input("Enter custom HTTP/s Port number: ")
		port=port_number
	else:
		print("Invalid selection. Using default port 80.")
		
	custom_thread=input("Do you want to change thread ? (y or n)(default=4)")
	if custom_thread=="y":
		th_count=input("Enter threading count : ")
		threading=th_count
		
	if user_menu_input==1:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password : ")
		link=input("provide link:username&password variable:invalid message\n eg. /login.php:username=^USER^&password=^PASS^:Login Failed")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-p",pass_name,ip,"-t",threading,"http-post-form",link,"-s",port])
		print("\n\n")
		
	if user_menu_input==2:
		u_name=input("Enter Username : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-l",u_name,"-P",pass_name,ip,"-t",threading,"http-post-form",link,"-s",port])
		print("\n\n")
	
	if user_menu_input==3:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password list : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-P",pass_name,ip,"-t",threading,"http-post-form",link,"-s",port])
		print("\n\n")
		
		
	if user_menu_input==4:
		u_name=input("Enter Username list : ")
		pass_name=input("Enter Password : ")
		print("\n\n")
		subprocess.call(["hydra","-f","-L",u_name,"-p",pass_name,ip,"-t",threading,"http-post-form",link,"-s",port])
		print("\n\n")

