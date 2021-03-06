#duplicated_kmeans_data.py
######################create data without remove repeated data

print("###################create data include result 0 or 1")
import numpy as np
import pandas as pd
data1= pd.read_csv('total_http_header_clustered.csv',header=None)
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
##########################break data into train data set and test data set
n=0
train=[]
test=[]
temp=s.values.tolist()
for i in temp:
    if n<560:
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
df1.to_csv('total_http_header_train_560_complete.csv',index=False)
df2=pd.DataFrame(test,columns=column)
df2.to_csv('total_http_header_test_183_complete.csv',index=False)
traindata= pd.read_csv('total_http_header_train_560_complete.csv',header=None)
testdata= pd.read_csv('total_http_header_test_183_complete.csv',header=None)
print(traindata)
print(testdata)

#############################################transport data file to specific value
import pandas as pd
import numpy as np
import os
textFile1=open('total_http_header_train_560_complete.csv','rb')
data= pd.read_csv(textFile1)
textFile2=open('total_http_header_test_183_complete.csv','rb')
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
for each in range(0,560):
    m=[]
    for i in result1:
        m.append(i[each])
    m1.append(m)


m2=[]
for each in range(0,183):
    m=[]
    for i in result2:
        m.append(i[each])
    m2.append(m)
#print(len(m1))   
#print(len(m2)) 

df1=pd.DataFrame(m1,columns=list1)
df1.to_csv('total_http_header_train_560_complete_convert.csv',index=False)
df2=pd.DataFrame(m2,columns=list1)
df2.to_csv('total_http_header_test_183_complete_convert.csv',index=False)
print("done")
traindata= pd.read_csv('total_http_header_train_560_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_test_183_complete_convert.csv',header=None)
print(traindata)
print(testdata)