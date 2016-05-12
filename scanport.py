#!/usr/bin/python
import socket
def scanport(ip,port):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		sock.connect((ip,port))
		print str(ip)+':'+str(port)
		sock.close()
	except:
		pass
portlist=[80,139,23,8080]
for i in portlist:
	scanport('192.168.50.1',i)
