#!/usr/bin/python
import re,urllib,socket
from bs4  import BeautifulSoup
socket.setdefaulttimeout(5)
domainarr=[]
def BDSS(keyword,num):
	try:
		BDUrl = "https://baidu.com/s?wd=%s&pn=%s" %(keyword,num*10)
		return urllib.urlopen(BDUrl).read()
	except KeyboardInterrupt:
		exit()
	except IOError:
		print 'error'
keyword='site:gov.cn'
for num in range(5):
	soup=BeautifulSoup(BDSS(keyword,num),'lxml')
	obj=soup.find_all("a",class_="c-showurl")
	for i in obj:
		try:
			URL=urllib.urlopen(i.get('href')).geturl()
			#URL=BeautifulSoup(urllib.urlopen(i.get('href')).read(),'lxml').find_all('noscript')[0].find_all('meta')[0].get('content').split(';')[1].split('\'')[1]
			ipstr=socket.gethostbyname(URL.split('/')[2])
			urlstr=URL+','+URL.split('/')[2]+','+ipstr+','+ipstr[:ipstr.rfind('.')]+'.0/24'
			print urlstr.split(',')
		except KeyboardInterrupt:
			exit()
		except IOError:
			print 'error'





