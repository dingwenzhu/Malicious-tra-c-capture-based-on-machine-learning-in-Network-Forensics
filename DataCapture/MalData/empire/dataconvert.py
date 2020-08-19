#!/usr/bin/python3
import os 
import sys
##url decode
f=open(sys.argv[1])
for i in f:
    a=os.popen('urlencode -d "'+i+'" >> newtempfile.txt')
f.close()

###add "key"
f=open("newtempfile.txt")
f1=open("temp","w")
for i in f:
    if "GET" in i:
        f1.write("=============================================================\n")
        i="method:"+i
    if "POST" in i:
        f1.write("=============================================================\n")
        i="method:"+i
    f1.write(i)
f1.close()

f.close()
os.system("sed /^\s*$/d temp > "+sys.argv[2])
os.system("rm -f newtempfile.txt && rm -f temp")
