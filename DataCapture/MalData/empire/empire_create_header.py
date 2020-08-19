#!/usr/bin/python3
import os
import time
while True:
    os.system("sudo nc -nvlp 80 >> http_header.txt &")
    a=os.popen("netstat -antp|grep nc|grep ESTABLISHED")
    while True:
        if a.read() == "":
            a=os.popen("netstat -antp|grep nc|grep ESTABLISHED")
        else:
            break
    a=os.popen("netstat -antp|grep nc|grep ESTABLISHED")
   # print(a.read())
    PID=a.read().split("/")[0][-5:]
    print(PID)
    os.system("kill -9 "+str(PID))
