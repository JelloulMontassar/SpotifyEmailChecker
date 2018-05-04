import requests
from bs4 import BeautifulSoup
import random
def freshproxies():
	vide = []
	proxies=[]
	m = list()
	session=requests.Session()
	url=session.get('https://www.sslproxies.org/')
	page= BeautifulSoup(url.text,'lxml')
	f = page.find('table')
	rows =f.findAll('tr')
	for tr in rows:
		cols  = tr.findAll('td')
		for td in cols:
			vide.append(td.text)
	for i in range(len(vide)):
		proxies.append(vide[0:2])
		del vide[0:8]	
	p = 0
	for key in proxies:
		p+=1
		if p ==100:
			break
		else:	
			m.append(key[0]+':'+key[1])
	return random.choice(m)		
