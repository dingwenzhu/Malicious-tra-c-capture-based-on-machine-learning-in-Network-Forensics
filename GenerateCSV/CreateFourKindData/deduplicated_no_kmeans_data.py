#deduplicated_no_kmeans_data.py 
#Change Database without kmeans
import os
import pandas as pd

import numpy as np

textFile=open('total_http_header.csv','rb')
data= pd.read_csv(textFile)
NumberOfKey=[]
for i in data['NumberOfKey']:
    if i < 10:
        i="low"
    elif 10<=i<15:
        i="mid"
    elif i>=15:
        i="high"
    NumberOfKey.append(i)
#print(NumberOfKey) 
data['NumberOfKey']=NumberOfKey
LengthOfRequest=[]
for i in data['LengthOfRequest']:
    if i < 317:
        i="low"
    elif 317<=i<619:
        i="mid"
    elif i>=511:
        i="high"
    LengthOfRequest.append(i)
#print(LengthOfRequest) 
data['LengthOfRequest']=LengthOfRequest
NumberOfSlashInRequest=[]
for i in data['NumberOfSlashInRequest']:
    if i < 7:
        i="low"
    elif 7<=i<12:
        i="mid"
    elif i>=12:
        i="high"
    NumberOfSlashInRequest.append(i)
#print(NumberOfSlashInRequest) 
data['NumberOfSlashInRequest']=NumberOfSlashInRequest
LengthOfAccept=[]
for i in data['LengthOfAccept']:
    if i < 35:
        i="low"
    elif 35<=i<70:
        i="mid"
    elif i>=70:
        i="high"
    LengthOfAccept.append(i)
#print(LengthOfAccept) 
data['LengthOfAccept']=LengthOfAccept
LengthOfContentLength=[]
for i in data['LengthOfContent-Length']:
    if i < 6870:
        i="low"
    elif  6870<=i<13739:
        i="mid"
    elif i>=13739:
        i="high"
    LengthOfContentLength.append(i)
#print(LengthOfContentLength) 
data['LengthOfContent-Length']=LengthOfContentLength

LengthOfContentType=[]
for i in data['LengthOfContent-Type']:
    if i < 29:
        i="low"
    elif 29<=i<59:
        i="mid"
    elif i>=59:
        i="high"
    LengthOfContentType.append(i)
#print(LengthOfContentType) 
data['LengthOfContent-Type']=LengthOfContentType

data.to_csv('total_http_header_nokmeans.csv',index=False)
print(data)

####################################################################################################################

print("###################create data include result 0 or 1")
data1= pd.read_csv('total_http_header_nokmeans.csv',header=None)
s=data1.drop([0],axis=1)
s=s.drop([0],axis=0)
temp=[]
for i in range(0,743):
    if i<443:
        temp.append(0)
    else:
        temp.append(1)


s[12]=temp
print(s)
print("##########################shuffle data")
##########################shuffle data
s = shuffle(s)
print(s)
print("##########################remove repeated data")
##########################remove repeated data
temp=[]
s=s.values.tolist()
for i in s:
    if i not in temp:
        temp.append(i)
print("data length="+str(len(temp)))
print("##########################break data into train data set and test data set")
##########################break data into train data set and test data set
n=0
train=[]
test=[]

for i in temp:
    if n<25:
        train.append(i)
    else:
        test.append(i)
    n+=1
print("train:")
print(np.array(train))
print("test:")
print(np.array(test))       

print("##########################create data file of trainset and testset")
##########################create data file of trainset and testset
#column=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','Result']
column=['ReuqestMethod','NumberOfKey','LengthOfRequest','NumberOfSlashInRequest','LengthOfAccept','LengthOfConnection','LengthOfContent-Length','LengthOfContent-Type','LengthOfAccept-Encoding','LengthOfAccept-Language','LengthOfCookie','Result']
df1=pd.DataFrame(train,columns=column)
df1.to_csv('total_http_header_nocluster_train_unique_25_complete.csv',index=False)
df2=pd.DataFrame(test,columns=column)
df2.to_csv('total_http_header_nocluster_test_unique_6_complete.csv',index=False)

traindata= pd.read_csv('total_http_header_nocluster_train_unique_25_complete.csv',header=None)
testdata= pd.read_csv('total_http_header_nocluster_test_unique_6_complete.csv',header=None)
print(traindata)
print(testdata)

#############################################################################################################
textFile1=open('total_http_header_nocluster_train_unique_25_complete.csv','rb')
data= pd.read_csv(textFile1)
textFile2=open('total_http_header_nocluster_test_unique_6_complete.csv','rb')
data2= pd.read_csv(textFile2)
#print(data)
def change(data):
    temp=['ReuqestMethod','NumberOfKey','LengthOfRequest','NumberOfSlashInRequest','LengthOfAccept','LengthOfConnection','LengthOfContent-Length','LengthOfContent-Type','LengthOfAccept-Encoding','LengthOfAccept-Language','LengthOfCookie','Result']
    #temp=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','Result']
    for each in temp:
        a=[]
        for i in data[each]:
            if i not in a:
                a.append(i)

        #print(each,a)
    #print("done")
    result=[]

    ReuqestMethod=[]
    for i in data['ReuqestMethod']:
        if i =='GET':
            ReuqestMethod.append('a11')
        else:
            ReuqestMethod.append('a12')
    result.append(ReuqestMethod) 

    NumberOfKey=[]
    for i in data['NumberOfKey']:
        if i =='low':
            NumberOfKey.append('a21')
        elif i == 'mid':
            NumberOfKey.append('a22')
        else:
            NumberOfKey.append('a23')
    result.append(NumberOfKey)


    LengthOfRequest=[]
    for i in data['LengthOfRequest']:
        if i =='low':
            LengthOfRequest.append('a31')
        elif i == 'mid':
            LengthOfRequest.append('a32')
        else:
            LengthOfRequest.append('a33')
    result.append(LengthOfRequest)

    NumberOfSlashInRequest=[]
    for i in data['NumberOfSlashInRequest']:
        if i =='low':
            NumberOfSlashInRequest.append('a41')
        elif i == 'mid':
            NumberOfSlashInRequest.append('a42')
        else:
            NumberOfSlashInRequest.append('a43')
    result.append(NumberOfSlashInRequest)

    LengthOfAccept=[]
    for i in data['LengthOfAccept']:
        if i =='low':
            LengthOfAccept.append('a51')
        elif i == 'mid':
            LengthOfAccept.append('a52')
        else:
            LengthOfAccept.append('a53')
    result.append(LengthOfAccept)

    LengthOfConnection=[]
    for i in data['LengthOfConnection']:
        if i ==7:
            LengthOfConnection.append('a61')
        elif i == 12:
            LengthOfConnection.append('a62')
        else:
            LengthOfConnection.append('a63')
    result.append(LengthOfConnection)

    LengthOfContentLength=[]
    for i in data['LengthOfContent-Length']:
        if i =='low':
            LengthOfContentLength.append('a71')
        elif i == 'mid':
            LengthOfContentLength.append('a72')
        else:
            LengthOfContentLength.append('a73')
    result.append(LengthOfContentLength)

    LengthOfContentType=[]
    for i in data['LengthOfContent-Type']:
        if i =='low':
            LengthOfContentType.append('a81')
        elif i =='mid':
            LengthOfContentType.append('a82')
        else:
            LengthOfContentType.append('a83')
    result.append(LengthOfContentType)

    LengthOfAcceptEncoding=[]
    for i in data['LengthOfAccept-Encoding']:
        if i ==15:
            LengthOfAcceptEncoding.append('a91')
        elif i == 0:
            LengthOfAcceptEncoding.append('a92')
        else:
            LengthOfAcceptEncoding.append('a93')
    result.append(LengthOfAcceptEncoding)

    LengthOfAcceptLanguage=[]
    for i in data['LengthOfAccept-Language']:
        if i ==16:
            LengthOfAcceptLanguage.append('aa1')
        else:
            LengthOfAcceptLanguage.append('aa2')
    result.append(LengthOfAcceptLanguage)

    LengthOfCookie=[]
    for i in data['LengthOfCookie']:
        if i ==0:
            LengthOfCookie.append('ab1')
        else:
            LengthOfCookie.append('ab2')
    result.append(LengthOfCookie)
    result.append(data['Result'])
    
    return result
list1=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','Result']
result1=change(data)
result2=change(data2)

m1=[]
for each in range(0,25):
    m=[]
    for i in result1:
        m.append(i[each])
    m1.append(m)


m2=[]
for each in range(0,6):
    m=[]
    for i in result2:
        m.append(i[each])
    m2.append(m)
#print(len(m1))   
#print(len(m2)) 

df1=pd.DataFrame(m1,columns=list1)
df1.to_csv('total_http_header_nocluster_train_unique_25_complete_convert.csv',index=False)
df2=pd.DataFrame(m2,columns=list1)
df2.to_csv('total_http_header_nocluster_test_unique_6_complete_convert.csv',index=False)
print("done")
traindata= pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert.csv',header=None)
print(traindata)
print(testdata)