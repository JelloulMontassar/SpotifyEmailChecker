from requests import Session
import random
from GETPROXIES import freshproxies
from termcolor import colored
import os
V = 0
N = 0
class Spotify:
	def Verify(self,email,a,b):
		self.vide = {}
		session = Session()
		self.email = email
		url='https://www.spotify.com/us/xhr/json/isEmailAvailable.php?email='
		req1= session.get(url.replace('?email=',''))
		getcookies = req1.cookies
		self.vide['https']=freshproxies()
		req = session.get(url+self.email,cookies=getcookies,proxies=self.vide,verify=True)
		if (req.text) == 'false':
			global V
			V+=1
			print(colored(('[{}/{}] '.format(b,a)+self.email),'green'))
			with open('SpotifyV.txt','a') as p:
				p.write(self.email+'\n')
				p.close()
		elif (req.text) == 'true':
			global N
			N+=1
			print(colored(('[{}/{}] '.format(b,a)+self.email),'red'))
			with open('SpotifyN.txt','a') as p:
				p.write(self.email+'\n')	
				p.close()	
def Email():
	o=list()
	try:
		print('ENTER MAILIST FILE (exp: emails.txt)')
		read = input(' > ')
		mails,m =  open(read,'r'),open(read,'r')
	except:
		Email()	
	NUM = 0	
	os.system('clear')
	for i in m :
		o.append(i)
	print('\t\t\tYOU GONNA CHECK {} EMAILS'.format(len(o)))	
	for email in mails:
		NUM+=1
		x = Spotify()
		f=email.replace('\n','')
		x.Verify(f,len(o),NUM)
	print('\t\t\t\tYOU HAVE CHECKED :{} '.format(NUM))	
	print('\t\t\t\tVALID EMAILS :{} '.format(V))	
	print('\t\t\t\tNOT VALID :{} '.format(N))	
Email()