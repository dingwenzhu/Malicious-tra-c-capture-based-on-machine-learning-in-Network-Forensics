#DecisionTree.py
#0>>normal traffic
#1>>malicious traffic
import pandas as pd
import numpy as np
import os
from math import log
import time

def CalEc(list1):
    s=0
    for i in list1:
        if i[-1] == '0':
            s+=1
    m=s/len(list1)
    n=1-m
    e=-(m*log(m,2)+n*log(n,2))
    return e
#a=CalEc(list1)
#print(a)
#print(len(list1))

def CalEcA1(list1):
    result=[]
    for k in range(len(list1[0])-1):
        temp1=[]
        temp2=[]
        a=[]
        for i in list1:
            temp1.append((i[k],i[-1]))
            temp2.append(i[k])
        temp2 = list(set(temp2))
        #print(temp2)
        for s in range(len(temp2)):
            a.append(s)
            a[s]=[]
            #print(a)
        d=0
        for b in temp2:
            for c in temp1:
                if c[0]==b:
                    a[d].append(c[1])
            d+=1
        result.append(a)
    return result

        

def CalEcA2(list2):
    a=CalEcA1(list2)
    temp=[]
    for b in a:
        m=[]
        for i in range(len(b)):
            n=0
            for each in b[i]:
                if each == '0':
                    n+=1
            m.append([n,len(b[i])])
        #print(m)
        v=0
        for r in m:
            v=v+r[1]
        #print(v)
        k=0
        for r in m:
            k1=r[0]/r[1]
            #print(k1)
            k2=1-k1
            #print(k2)
            if k1 == 0:
                k=k+(k2)*log((k2),2)*(r[1]/v)
            elif k2 == 0:
                k=k+(k1)*log((k1),2)*(r[1]/v)
            else:
                k=k+((k1)*log((k1),2)+(k2)*log((k2),2))*(r[1]/v)
        temp.append(-k)
    return temp


def GRc(list1):
    r=[]
    for w in range(len(list1[0])-1):
        m=[]
        for i in list1:
            i=i[w]
            #print(i)
            m.append(i)
        m1 = list(set(m))
        s=0
        for each in m1:
            a=m.count(each)
            if a!=0:
                b=(a/len(m))*log((a/len(m)),2)
            s=s+b

        r.append(-s)
    return r
    
        
#a=CalEcA2(list1)
#print(a)
#b=CalEc(list1)
#print(b)
#a=GRc(list1)
#print(type(a))
def ChooseTree(list1):
    
    Ec=CalEc(list1)
    Eca=CalEcA2(list1)
    grc=GRc(list1)
    temp=[]
    n=0
    for i in Eca:
        #print(Ec-i)
        #print(grc[n])
        if grc[n] !=0:
            
            result= (Ec-i)/grc[n]
        else:
            result=0
        #index=hlist1[0][n]
        temp.append(result)
        n+=1
    index=hlist1[0]
    temp1=dict(zip(index,temp))
    #print(temp1)
    a=max(temp1.values())
    for key,value in temp1.items():
        if value ==a:
            #print(key)
            return (key,value)
    #return temp1

def SperateData(a,newlist):#input ChooseTree(list1)
    n=0
    for i in hlist1[0]:
        if i ==a[0]:
            break
        n+=1
    #print('n='+str(n))
    temp=[]
    for h in newlist:
        temp.append(h[n])
    temp1= list(set(temp))
    index=[]
    for i in range(len(temp1)):
        index.append(i)
        index[i]=[]
    x=0   
    for each in temp1:
        for i in newlist:
            if each ==i[n]:
                index[x].append(i)
        x+=1
    print(temp1)
    return index,temp1

            

def DiagnoseClass(x):
    temp=[]
    for i in x:
        c=temp.append(i[-1])
    c=list(set(temp))
    return c
    
            
def DiffClass(b):#input SperateData(a)
    n=0
    temp=[]
    for i in b[0]:
        c=DiagnoseClass(i)
        #print('DiagnoseClass'+str(c))
        if len(c)==2:
            print(b[1][n]+' not same class,calculate it')
            temp.append([b[1][n],b[0][n]])
        else:
            print((b[1][n]+'='+c[0]))
    
        n+=1  #cycle till  temp==[]  
    return temp    
########################################CreateDecisionTree(deduplicated,cluster)
print("########################################CreateDecisionTree(deduplicated,cluster)")
start_time=time.time()
data1= pd.read_csv('total_http_header_train_unique_36_complete_convert.csv',header=None)
hlist1=data1.values.tolist()
list1=hlist1[1:]

data2= pd.read_csv('total_http_header_test_unique_9_complete_convert.csv',header=None)
hlist2=data2.values.tolist()
list2=hlist2[1:]

a=ChooseTree(list1)
print('root is '+a[0])
b=SperateData(a,list1)
for each in range(len(b[1])):
    print('branch='+b[1][each])
c=DiffClass(b)

while len(c)!=0:
    for i in c:

        a=ChooseTree(i[1])
        print('root is '+a[0])
        b=SperateData(a,i[1])
        for each in range(len(b[1])):
            print('branch='+b[1][each])
        c=DiffClass(b)
    
print("end")


#DiagnoseDecisionTree

count=0
for i in list2:
    if i[9]=='aa1':
        if i[11]=='0':
            count +=1
    elif i[9]=='aa2':
        if i[11]=='1':
            count +=1
end_time=time.time()
print("time:"+str(end_time-start_time))
print("accuracy rate:") 
print(count/len(list2))


########################################CreateDecisionTree(duplicated,cluster)
print("########################################CreateDecisionTree(duplicated,cluster)")
start_time=time.time()
data1= pd.read_csv('total_http_header_train_560_complete_convert.csv',header=None)
hlist1=data1.values.tolist()
list1=hlist1[1:]

data2= pd.read_csv('total_http_header_test_183_complete_convert.csv',header=None)
hlist2=data2.values.tolist()
list2=hlist2[1:]

a=ChooseTree(list1)
print('root is '+a[0])
b=SperateData(a,list1)
for each in range(len(b[1])):
    print('branch='+b[1][each])
c=DiffClass(b)

while len(c)!=0:
    for i in c:

        a=ChooseTree(i[1])
        print('root is '+a[0])
        b=SperateData(a,i[1])
        for each in range(len(b[1])):
            print('branch='+b[1][each])
        c=DiffClass(b)
    
print("end")

#DiagnoseDecisionTree
count=0
for i in list2:
    if i[9]=="aa1":
        if i[11]=="0":
            count+=1
    elif i[9]=="aa2":
        if i[3]=='a41':
            if i[11]=='1':
                count +=1
        elif i[3]=='a42':
            if i[11]=='0':
                count +=1
end_time=time.time()
print("time:"+str(end_time-start_time))
print("accuracy rate:")
print(count/len(list2))
########################################CreateDecisionTree(deduplicated,no-cluster)
print("########################################CreateDecisionTree(deduplicated,no-cluster)")
start_time=time.time()
#print(start_time)
data1= pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert.csv',header=None)
hlist1=data1.values.tolist()
list1=hlist1[1:]

data2= pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert.csv',header=None)
hlist2=data2.values.tolist()
list2=hlist2[1:]

a=ChooseTree(list1)
print('root is '+a[0])
b=SperateData(a,list1)
for each in range(len(b[1])):
    print('branch='+b[1][each])
c=DiffClass(b)

while len(c)!=0:
    for i in c:

        a=ChooseTree(i[1])
        print('root is '+a[0])
        b=SperateData(a,i[1])
        for each in range(len(b[1])):
            print('branch='+b[1][each])
        c=DiffClass(b)
    
print("end")

#DiagnoseDecisionTree
count=0
for i in list2:
    if i[9]=='aa1':
        if i[11]=='0':
            count +=1
    elif i[9]=='aa2':
        if i[11]=='1':
            count +=1
end_time=time.time()
#print(end_time)
print("time:"+str(end_time-start_time))
print("accuracy rate:")            
print(count/len(list2))
########################################CreateDecisionTree(duplicated,no-cluster)
print("########################################CreateDecisionTree(duplicated,no-cluster)")
start_time=time.time()
data1= pd.read_csv('total_http_header_nocluster_train_560_complete_convert.csv',header=None)
hlist1=data1.values.tolist()
list1=hlist1[1:]

data2= pd.read_csv('total_http_header_nocluster_test_183_complete_convert.csv',header=None)
hlist2=data2.values.tolist()
list2=hlist2[1:]

a=ChooseTree(list1)
print('root is '+a[0])
b=SperateData(a,list1)
for each in range(len(b[1])):
    print('branch='+b[1][each])
c=DiffClass(b)

while len(c)!=0:
    for i in c:

        a=ChooseTree(i[1])
        print('root is '+a[0])
        b=SperateData(a,i[1])
        for each in range(len(b[1])):
            print('branch='+b[1][each])
        c=DiffClass(b)
    
print("end")

#DiagnoseDecisionTree
count=0
for i in list2:
    if i[9]=='aa1':
        if i[11]=='0':
            count +=1
    elif i[9]=='aa2':
        if i[8]=='a92':
            if i[11]=='1':
                count+=1
        if i[8]=='a91':
            if i[11]=='0':
                count +=1
        if i[8]=='a93':
            if i[11]=='1':
                count +=1
                
end_time=time.time()
print("time:"+str(end_time-start_time))
print("accuracy rate:")            
print(count/len(list2))