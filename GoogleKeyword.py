#!/usr/bin/python
import re,urllib,socket
from bs4  import BeautifulSoup
socket.setdefaulttimeout(5)
def BDSS(keyword,num):
	BDUrl = "https://baidu.com/s?wd=%s&pn=%s" %(keyword,num*10)
	return urllib.urlopen(BDUrl).read()
keyword='site:gov.cn'
for num in range(5):
	soup=BeautifulSoup(BDSS(keyword,num))
	obj=soup.find_all("a",class_="c-showurl")
	for i in obj:
		print BeautifulSoup(urllib.urlopen(i.get('href')).read()).find_all('noscript')[0].find_all('meta')[0].get('content').split(';')[1].split('\'')[1]





