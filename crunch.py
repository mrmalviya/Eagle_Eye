import subprocess


def without_char():
	'''
	
	'''
	min_len=input("\033[1;35;40mProvide minimum length : \033[1;m")
	max_len=input("\n\033[1;35;40mProvide maximum length : \033[1;m")
	filename=input("\n\033[1;35;40mProvide output file name : \033[1;m")
	subprocess.call(["crunch",min_len,max_len,"-o",filename])
	
def with_char():
	min_len=input("\033[1;35;40mProvide minimum length : \033[1;m")
	max_len=input("\n\033[1;35;40mProvide maximum length : \033[1;m")
	char_set=input("\n\033[1;35;40mEnter character set (you can refer char.txt)\033[1;m")
	filename=input("\n\033[1;35;40mProvide output file name : eg. filename.txt\033[1;m")
	subprocess.call(["crunch",min_len,max_len,char_set,"-o",filename])
	
def with_pattern():
	min_len=input("\033[1;35;40mProvide minimum length : \033[1;m")
	max_len=input("\n\033[1;35;40mProvide maximum length : \033[1;m")
	patt=input("\033[1;35;40mEnter pattern \nUse @ for lowercase alphabets\nUse , for uppercase alphabets\nUse % for numeric character\nUse ^ for special character symbol\n\033[1;m")
	filename=input("\n\033[1;35;40mProvide output file name : eg. filename.txt\033[1;m")
	subprocess.call(["crunch",min_len,max_len,"-t",patt,"-o",filename])
	
def permutation():
	min_len=input("\033[1;35;40mProvide minimum length : \033[1;m")
	max_len=input("\n\033[1;35;40mProvide maximum length : \033[1;m")
	filename=input("\n\033[1;35;40mProvide output file name : eg. filename.txt : \033[1;m")
	first_st=input("\n\033[1;35;40mEnter First String : \033[1;m")
	second_st=input("\n\033[1;35;40mEnter Second String : \033[1;m")
	subprocess.call(["\033[1;35;40mcrunch",min_len,max_len,"-p",first_st,second_st,"-o",filename])
	
