#!/usr/bin/python3
import pandas as pd

def GetValue(x):
    temp=[]
    temp.append(x['method'].split(" ")[0])
    temp.append(len(x))
    temp.append(len(x['method']))
    temp.append(x['method'].count("/"))
    if 'Accept' in x.keys():
        temp.append(len(x['Accept']))
    else:
        temp.append(0)
    if 'Connection' in x.keys():
        temp.append(len(x['Connection']))
    else:
        temp.append(0)
    if 'Content-Length' in x.keys():
        temp.append(int(x['Content-Length']))
    else:
        temp.append(0)
    if 'Content-Type' in x.keys():
        temp.append(len(x['Content-Type']))
    else:
        temp.append(0)
    if 'Accept-Encoding' in x.keys():
        temp.append(len(x['Accept-Encoding']))
    else:
        temp.append(0)
    if 'Accept-Language' in x.keys():
        temp.append(len(x['Accept-Language']))
    else:
        temp.append(0)
    if 'Cookie' in x.keys():
        temp.append(len(x['Cookie']))
    else:
        temp.append(0)
    return temp


def GetDict(f):
    dict={}
    for i in f:
        dict[i.split(":")[0]]=i.split(":")[1]
    return(dict)



f=open("normal_http_header.txt")
f1=open("msf_http_header.txt")
f2=open("cobaltstrike_http_header.txt")
f3=open("empire_http_header.txt")

a=[]
result=[]
for i in f:
    if i[:1] !="=":
        a.append(i)
        continue
    else:
        test=GetDict(a)
        value=GetValue(test)
        result.append(value)
        a=[]
for i in f1:
    if i[:1] !="=":
        a.append(i)
        continue
    else:
        test=GetDict(a)
        value=GetValue(test)
        result.append(value)
        a=[]
for i in f2:
    if i[:1] !="=":
        a.append(i)
        continue
    else:
        test=GetDict(a)
        value=GetValue(test)
        result.append(value)
        a=[]
for i in f3:
    if i[:1] !="=":
        a.append(i)
        continue
    else:
        test=GetDict(a)
        value=GetValue(test)
        result.append(value)
        a=[]

f.close()
f1.close()
f2.close()
f3.close()
def CreateCSV(result):
    name=['ReuqestMethod','NumberOfKey','LengthOfRequest','NumberOfSlashInRequest','LengthOfAccept','LengthOfConnection','LengthOfContent-Length','LengthOfContent-Type','LengthOfAccept-Encoding','LengthOfAccept-Language','LengthOfCookie']
    CSV=pd.DataFrame(columns=name,data=result)
    return CSV

database=CreateCSV(result)
print(database)
database.to_csv("total_http_header.csv")
