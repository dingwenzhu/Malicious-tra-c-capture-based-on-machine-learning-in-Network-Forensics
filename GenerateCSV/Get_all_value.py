#Get_all_value.py
import os
import pandas as pd
textFile=open('total_http_header.csv','rb')
data= pd.read_csv(textFile)
temp=['ReuqestMethod','NumberOfKey','LengthOfRequest','NumberOfSlashInRequest','LengthOfAccept','LengthOfConnection','LengthOfContent-Length','LengthOfContent-Type','LengthOfAccept-Encoding','LengthOfAccept-Language','LengthOfCookie']
#temp=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','Result']
for each in temp:
    a=[]
    for i in data[each]:
        if i not in a:
            a.append(i)

    print(each,a)
    print(each,max(a))
    print(each,min(a))
    if each=='NumberOfKey':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
    if each=='LengthOfRequest':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
    if each=='NumberOfSlashInRequest':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
    if each=='LengthOfAccept':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
    if each=='LengthOfContent-Length':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
    if each=='LengthOfContent-Type':
        print((max(a)-min(a))/3+min(a),(max(a)-min(a))/3+min(a)+(max(a)-min(a))/3)
print("done")