#!/usr/bin/python3
import os
f=open("normaldata4.txt")
f1=open("cobaltstrike_http_header.txt")
f2=open("empire_http_header.txt")
f3=open("msf_http_header.txt")
temp=[]
f4=open("key.txt","w")
for i in f:
    if "GET" not in i:
        if "POST" not in i:
            if "========" not in i:
                a=i.split(":")[0]
                if a not in temp:
                    temp.append(a)
for i in f1:
    if "GET" not in i:
        a=i.split(":")[0]
        if a not in temp:
            temp.append(a)
for i in f2:
    if "GET" not in i:
        a=i.split(":")[0]
        if a not in temp:
            temp.append(a)
for i in f3:
    if "GET" not in i:
        a=i.split(":")[0]
        if a not in temp:
            temp.append(a)

print(temp)
for i in temp:

    f4.write(i)
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
