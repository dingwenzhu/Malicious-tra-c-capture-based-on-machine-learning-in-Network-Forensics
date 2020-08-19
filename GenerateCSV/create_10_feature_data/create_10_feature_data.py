#create_10_feature_data.py
#import pandas as pd
#############################################create multiple data with 10 features
print("#############################################create multiple data with 10 features")
traindata= pd.read_csv('total_http_header_train_560_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_test_183_complete_convert.csv',header=None)

for i in range(0,11):
    temp=traindata.drop([i],axis=1)
    temp.to_csv('total_http_header_train_560_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check1=pd.read_csv('total_http_header_train_560_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check1)
print("######################################test data")    
for i in range(0,11):
    temp=testdata.drop([i],axis=1)
    temp.to_csv('total_http_header_test_183_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check2=pd.read_csv('total_http_header_test_183_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check2)
    

#############################################create multiple data with 10 features
print("#############################################create multiple data with 10 features")
traindata= pd.read_csv('total_http_header_train_unique_36_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_test_unique_9_complete_convert.csv',header=None)

for i in range(0,11):
    temp=traindata.drop([i],axis=1)
    temp.to_csv('total_http_header_train_unique_36_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check1=pd.read_csv('total_http_header_train_unique_36_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check1)
print("######################################test data")    
for i in range(0,11):
    temp=testdata.drop([i],axis=1)
    temp.to_csv('total_http_header_test_unique_9_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check2=pd.read_csv('total_http_header_test_unique_9_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check2)
    

#############################################create multiple data with 10 features no kmeans repeat data
print("#############################################create multiple data with 10 features")
traindata= pd.read_csv('total_http_header_nocluster_train_560_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_nocluster_test_183_complete_convert.csv',header=None)

for i in range(0,11):
    temp=traindata.drop([i],axis=1)
    temp.to_csv('total_http_header_nocluster_train_560_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check1=pd.read_csv('total_http_header_nocluster_train_560_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check1)
print("######################################test data")    
for i in range(0,11):
    temp=testdata.drop([i],axis=1)
    temp.to_csv('total_http_header_nocluster_test_183_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check2=pd.read_csv('total_http_header_nocluster_test_183_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check2)
    
    
#############################################create multiple data with 10 features no kmeans no repeat data
print("#############################################create multiple data with 10 features")
traindata= pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert.csv',header=None)

for i in range(0,11):
    temp=traindata.drop([i],axis=1)
    temp.to_csv('total_http_header_nocluster_train_unique_25_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check1=pd.read_csv('total_http_header_nocluster_train_unique_25_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check1)
print("######################################test data")    
for i in range(0,11):
    temp=testdata.drop([i],axis=1)
    temp.to_csv('total_http_header_nocluster_test_unique_6_complete_convert_removeA'+str(i+1)+'.csv',index=False,header=None)
    check2=pd.read_csv('total_http_header_nocluster_test_unique_6_complete_convert_removeA'+str(i+1)+'.csv',header=None)
    print("==================================================")
    print(check2)

    
##################################################create data with remove A7A10 features
print("##################################################create data with remove A7 A10 features")
traindata= pd.read_csv('total_http_header_train_560_complete_convert.csv',header=None)
testdata= pd.read_csv('total_http_header_test_183_complete_convert.csv',header=None)

print("######################################train data")
temp=traindata.drop([6,9],axis=1)
temp.to_csv('total_http_header_train_560_complete_convert_removeA7A10.csv',index=False,header=None)
check1=pd.read_csv('total_http_header_train_560_complete_convert_removeA7A10.csv',header=None)
print(check1)
print("######################################test data")    

temp=testdata.drop([6,9],axis=1)
temp.to_csv('total_http_header_test_183_complete_convert_removeA7A10.csv',index=False,header=None)
check2=pd.read_csv('total_http_header_test_183_complete_convert_removeA7A10.csv',header=None)

print(check2)