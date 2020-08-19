#!/usr/bin/python3
import os 
import sys
f=open("test","w")
f.write("$data = artifact(\"test\",\"exe\");")
for i in range(1,101):
    f.write("$handle = openf(\">out"+str(i)+".exe\");"+"\n")
    f.write("writeb($handle,$data);"+"\n")
    f.write("closef($handle);"+"\n")
f.close()

