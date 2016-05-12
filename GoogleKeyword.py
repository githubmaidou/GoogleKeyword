#!/usr/bin/python
#-*- coding:utf-8 –*-
import re,urllib,socket,sys
from bs4  import BeautifulSoup
socket.setdefaulttimeout(5)
domainarr=[]
keyword='site:ncfgroup.com'
def BDSS(keyword,num):
	try:
		BDUrl = "https://baidu.com/s?wd=%s&pn=%s" %(keyword,num*10)
		return urllib.urlopen(BDUrl).read()
	except KeyboardInterrupt:
		exit()
	except IOError:
		print 'error'
def SS(l=5):
	num=l
	for num in range(num):
		soup=BeautifulSoup(BDSS(keyword,num),'lxml')
		obj=soup.find_all("a",class_="c-showurl")
		pc=soup.find_all("span",class_="pc")
		if num==int(pc[-1].text):
			exit()
		for i in obj:
			try:
				URL=urllib.urlopen(i.get('href')).geturl()
				#URL=BeautifulSoup(urllib.urlopen(i.get('href')).read(),'lxml').find_all('noscript')[0].find_all('meta')[0].get('content').split(';')[1].split('\'')[1]
				ipstr=socket.gethostbyname(URL.split('/')[2])
				urlstr=URL+','+URL.split('/')[2]+','+ipstr+','+ipstr[:ipstr.rfind('.')]+'.0/24'
				domainarr.append(urlstr.split(','))
			except KeyboardInterrupt:
				exit()
			except IOError:
				pass
		print '正在搜索第 '+str(num+1)+' 页..........采集到 '+str(len(domainarr))+' 条数据'
ssdic={}
ssnum=0
tagdic={'url':0,'domain':1,'ip':2,'ips':3}
for i in sys.argv:
	ssdic[i]=ssnum
	ssnum+=1
if '-h' in ssdic or '-help' in ssdic:
	print '-keyowrd 需要搜索的关键字'
	print '-l 需要搜索多少页,默认5页'
	print '-t 输出内容详细'
	print '		url 完整的URL链接'
	print '		domain 主域名'
	print '		ip 域名解析到的IP'
	print '		ips ip所在C段 127.0.0.0/24'
	print sys.argv[0]+' -keyword baidu -l 10 -t ipc'
	exit()
if '-keyword' in ssdic:
	keyword=sys.argv[ssdic['-keyword']+1]
else:
	print '缺少关键字 -keyword'
	print '-h or -help 查看使用方法' 
	exit()
if '-l' in ssdic and int(sys.argv[ssdic['-l']+1])>0:
	SS(int(sys.argv[ssdic['-l']+1]))
else:
	SS()
if '-t' in ssdic and sys.argv[ssdic['-t']+1] in tagdic:
	for i in domainarr:
		print i[tagdic[sys.argv[ssdic['-t']+1]]]
else:
	for i in domainarr:
		print i
	
	
