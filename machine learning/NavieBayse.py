#NavieBayse.py
#0>>normal traffic
#1>>malicious traffic
import pandas as pd
import numpy as np
import os
from functools import reduce
from operator import mul
import time



def CalKnownPriority(list1):   
    total=[]
    for i in range(0,len(list1[0])-1):
        temp=[]
        templist=[]
        for a in list1:
            temp.append(a[i])
        temp1 = list(set(temp))
        #print(temp1)
        for h in temp1:
            s=temp.count(h)
            templist.append([h,round(s/len(list1),3)])
        
        total=total+templist
    return total



def CalNewPriority(x,list1):
    NorData=[]
    MalData=[]
    for i in list1:
        if i[-1] == '0':
            NorData.append(i)
        else:
            MalData.append(i)
    
    Pc1=len(NorData)/len(list1)
    Pc2=len(MalData)/len(list1)
    #print(Pc1,Pc2)
    a=CalKnownPriority(NorData)
    #print(a)
    
    b=CalKnownPriority(MalData)
    #print(b)
    temp1=[]
    temp2=[]

    for each in x:
        for i in a:
            if i[0] ==each:
                temp1.append(i[1])
    #print(len(temp1))
    for each in x:
        for i in b:
            if i[0] ==each:
                temp2.append(i[1])
    #print(len(temp2))
    if len(temp1)<len(x):
        a1=0
    else:
        a1 = reduce(mul, temp1, 1)*Pc1
    if len(temp2)<len(x):
        a2=0
    else:
        a2 = reduce(mul, temp2, 1)*Pc2
    if a1 > a2:
        return 0
    else:
        return 1
        


def CalAccuracy(list2,list1):
    start_time=time.time()
    n=0
    for i in list2:
        a=i[0:-1]
        #print(a)
        result=CalNewPriority(a,list1)
        if str(result)==i[-1]:
            n+=1
    end_time=time.time()
    print("time:"+str(end_time-start_time))
    return n/len(list2)


###################################################Accuracy of whole features(deduplicated,cluster)

temp1=[]
temp2=[]
data1= pd.read_csv('total_http_header_train_unique_36_complete_convert.csv',header=None)
list1=data1.values.tolist()
list1=list1[1:]
#print(np.array(list1))

data2= pd.read_csv('total_http_header_test_unique_9_complete_convert.csv',header=None)
list2=data2.values.tolist()
list2=list2[1:]
#print(np.array(list2))
result=CalAccuracy(list2,list1)

print("accuracy of whole features(cluster,deduplicated):")
print(result)
print("==================================")
###################################################Accuracy of 10 features(deduplicated,cluster)
print("Accuracy of 10 features(cluster,deduplicated)")
for i in range(0,11):
    traindata=pd.read_csv('total_http_header_train_unique_36_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    testdata=pd.read_csv('total_http_header_test_unique_9_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    listtrain=traindata.values.tolist()
    listtrain=listtrain[1:]
    listtest=testdata.values.tolist()
    listtest=listtest[1:]
    """
    print(np.array(listtrain))
    print("===================================================")

    print(np.array(listtest))
    print("===================================================")
    """
    result=CalAccuracy(listtest,listtrain)
    
    print("accuracy of removeA"+str(i+1)+" features")
    print(result)


print("==================================")

###################################################Accuracy of whole features(duplicated,cluster)
temp1=[]
temp2=[]
data1= pd.read_csv('total_http_header_train_560_complete_convert.csv',header=None)
list1=data1.values.tolist()
list1=list1[1:]
#print(np.array(list1))

data2= pd.read_csv('total_http_header_test_183_complete_convert.csv',header=None)
list2=data2.values.tolist()
list2=list2[1:]
#print(np.array(list2))
result=CalAccuracy(list2,list1)
print("accuracy of whole features(cluster,duplicated):")
print(result)
print("==================================")
###################################################Accuracy of 10 features(duplicated,cluster)
print("Accuracy of 10 features(cluster,duplicated)")
for i in range(0,11):
    traindata=pd.read_csv('total_http_header_train_560_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    testdata=pd.read_csv('total_http_header_test_183_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    listtrain=traindata.values.tolist()
    listtrain=listtrain[1:]
    listtest=testdata.values.tolist()
    listtest=listtest[1:]
    """
    print(np.array(listtrain))
    print("===================================================")

    print(np.array(listtest))
    print("===================================================")
    """
    result=CalAccuracy(listtest,listtrain)
    
    print("accuracy of removeA"+str(i+1)+" features no deduplicate")
    print(result)
print("==================================")
#########################################################Accuracy of whole features(deduplicated,no-cluster)

data1= pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert.csv',header=None)
list1=data1.values.tolist()
list1=list1[1:]
#print(np.array(list1))

data2= pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert.csv',header=None)
list2=data2.values.tolist()
list2=list2[1:]
#print(np.array(list2))
result=CalAccuracy(list2,list1)
print("accuracy of whole features(no-cluster,deduplicated):")
print(result)
print("==================================")
###################################################################Accuracy of 10 features(deduplicated,no-cluster)
print("Accuracy of 10 features(no-cluster,deduplicated)")
for i in range(0,11):
    traindata=pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    testdata=pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    listtrain=traindata.values.tolist()
    listtrain=listtrain[1:]
    listtest=testdata.values.tolist()
    listtest=listtest[1:]
    """
    print(np.array(listtrain))
    print("===================================================")

    print(np.array(listtest))
    print("===================================================")
    """
    result=CalAccuracy(listtest,listtrain)
    
    print("accuracy of removeA"+str(i+1)+" features")
    print(result)


print("==================================")

########################################################################Accuracy of whole features(duplicated,no-cluster)
print("accuracy of no-kmeans,duplicated")
data1= pd.read_csv('total_http_header_nocluster_train_560_complete_convert.csv',header=None)
list1=data1.values.tolist()
list1=list1[1:]
#print(np.array(list1))

data2= pd.read_csv('total_http_header_nocluster_test_183_complete_convert.csv',header=None)
list2=data2.values.tolist()
list2=list2[1:]
#print(np.array(list2))
result=CalAccuracy(list2,list1)
print("accuracy of whole features(no-cluster,duplicated):")
print(result)
print("==================================")
############################################################################Accuracy of 10 features(duplicated,no-cluster)
print("Accuracy of 10 features(no-kmeans,duplicated)")
for i in range(0,11):
    traindata=pd.read_csv('total_http_header_nocluster_train_560_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    testdata=pd.read_csv('total_http_header_nocluster_test_183_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    listtrain=traindata.values.tolist()
    listtrain=listtrain[1:]
    listtest=testdata.values.tolist()
    listtest=listtest[1:]
    """
    print(np.array(listtrain))
    print("===================================================")

    print(np.array(listtest))
    print("===================================================")
    """
    result=CalAccuracy(listtest,listtrain)
    
    print("accuracy of removeA"+str(i+1)+" features")
    print(result)
print("==================================")
###################################################Accuracy without A7A10 features(deduplicated)    
print("###################################")
print("data without A7A10")
data_train_A7A10=pd.read_csv('total_http_header_train_unique_36_complete_convert_removeA7A10.csv',header=None)
data_test_A7A10=pd.read_csv('total_http_header_test_unique_9_complete_convert_removeA7A10.csv',header=None)
list_data_train_A7A10=data_train_A7A10.values.tolist()
list_data_test_A7A10=data_test_A7A10.values.tolist()
list_data_train_A7A10=list_data_train_A7A10[1:]
list_data_test_A7A10=list_data_test_A7A10[1:]
result=CalAccuracy(list_data_test_A7A10,list_data_train_A7A10)
print(result)

###################################################Accuracy without A7A10 features    
print("###################################")
print("data without A7A10")

data_train_A7A10=pd.read_csv('total_http_header_train_560_complete_convert_removeA7A10.csv',header=None)
data_test_A7A10=pd.read_csv('total_http_header_test_183_complete_convert_removeA7A10.csv',header=None)
list_data_train_A7A10=data_train_A7A10.values.tolist()
list_data_test_A7A10=data_test_A7A10.values.tolist()
list_data_train_A7A10=list_data_train_A7A10[1:]
list_data_test_A7A10=list_data_test_A7A10[1:]
result=CalAccuracy(list_data_test_A7A10,list_data_train_A7A10)

print(result)
