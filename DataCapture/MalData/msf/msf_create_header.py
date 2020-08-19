#!/usr/bin/python3
import os
import time
n=0
while n<101: 
    os.system("sudo nc -nvlp 80 >> http_header.txt &")
    os.system("python pythonreverse"+str(n)+".py")
    time.sleep(4)
    a=os.popen("netstat -antp|grep python")
    PID=a.read().split("/")[0][-4:]
    print(PID)
    os.system("kill -9 "+str(PID))
    n +=1
