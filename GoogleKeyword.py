#!/usr/bin/python
import re,urllib
from bs4  import BeautifulSoup
def BDSS(keyword,num):
	BDUrl = "http://baidu.com/s?wd=%s&pn=%s" %(keyword,num*10)
	return urllib.urlopen(BDUrl).read()
keyword='youtube'
for num in range(76):
	soup=BeautifulSoup(BDSS(keyword,num))
	obj=soup.find_all("a",class_="c-showurl")
	for i in obj:
		print  i.text.encode('utf8')
		print  i.text.split('/')[0]
		print  "--------------------"





