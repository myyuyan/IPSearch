import subprocess
import threading
import time
import socket
n=0
class my(threading.Thread):
	def __init__(self,ip):
		threading.Thread.__init__(self)
		self.ip=ip
	def run(self):
		IPSearch(self.ip)
def IPSearch(ip):
	global n
	cmdstr = "ping "+ip+" -n 1 -w 50"
	pr=0x00000008
	try:
		subprocess.run(cmdstr,creationflags=pr,check=True)
	except subprocess.CalledProcessError as err:
		ne=err
	else:
		try:
			result=socket.gethostbyaddr(ip)
			result=result[0]
		except:
			result="未找到"
		print("IP:"+ip+"   主机名:"+result)
		n+=1
i=0
while i<255:
	i+=1
	ipstr="10.241.135."+str(i)#输入要检测的IP网段
	t=my(ipstr)
	t.start()
while True:
	length=len(threading.enumerate())
	time.sleep(1)
	if length<=1:
		break
print("在线主机数："+str(n))