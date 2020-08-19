import matplotlib.pyplot as plt
import pandas as pd
import os
%matplotlib inline

result=[]
s=[0, 35, 26, 88, 18, 12]
for i in s:
    result.append([i,i])
#print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('LengthOfContentType.csv')
csv=pd.read_csv('LengthOfContentType.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) 
ax.set_xlabel('LengthOfContentType')
ax.set_ylabel('LengthOfContentType')
plt.show()




result=[]
s=[5,6,7,8,9,11,10,20,12]
for i in s:
    result.append([i,i])
#print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('NumberOfKey.csv')
csv=pd.read_csv('NumberOfKey.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) 
ax.set_xlabel('NumberOfKey')
ax.set_ylabel('NumberOfKey')
plt.show()




result=[]
s=['19', '23', '32', '28', '162', '130', '95', '195', '118', '61', '220', '228', '267', '240', '148', '141', '213', '268', '91', '266', '58', '47', '234', '200', '134', '143', '54', '250', '182', '169', '115', '89', '114', '160', '224', '212', '153', '190', '170', '269', '105', '232', '217', '80', '155', '158', '168', '229', '201', '101', '191', '146', '51', '129', '239', '208', '67', '126', '110', '227', '70', '242', '77', '245', '194', '178', '237', '258', '207', '249', '52', '187', '76', '108', '92', '151', '192', '147', '241', '180', '109', '59', '139', '136', '179', '78', '74', '72', '73', '66', '69', '65', '75', '48', '49', '33', '84', '30', '44', '40', '43', '63', '50', '38', '122', '82', '64', '34', '121', '289', '127', '310', '340', '62', '21', '41', '99', '29', '26', '46', '231', '55', '53', '177', '235', '37', '86', '24', '17', '71', '90', '57', '68', '42', '198', '171', '176', '175', '283', '135', '79', '27', '152', '60', '159', '150', '290', '56', '104', '387', '378', '45', '87', '233', '81', '921', '846', '137', '116', '174', '132', '144', '96', '106', '133', '83', '93', '120', '761', '754', '722', '647', '372', '337', '400', '142', '140', '138', '119', '35', '338', '15', '204', '414', '354', '330', '218', '222']
for i in s:
    result.append([int(i),int(i)])
#print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('LengthOfRequest.csv')
csv=pd.read_csv('LengthOfRequest.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) #ª≠…¢µ„Õº
ax.set_xlabel('LengthOfRequest')
ax.set_ylabel('LengthOfRequest')
plt.show()



s=['2', '3', '10', '6', '7', '8', '4', '5', '1', '9', '18', '13', '14', '12', '11', '15']
result=[]
for i in s:
    result.append([int(i),int(i)])
#print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('NumberOfSlashInRequest.csv')
csv=pd.read_csv('NumberOfSlashInRequest.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) #ª≠…¢µ„Õº
ax.set_xlabel('NumberOfSlashInRequest')
ax.set_ylabel('NumberOfSlashInRequest')
plt.show()


s=['0', '2013', '4243', '2540', '694', '5378', '544', '20609', '634', '1861', '494']
result=[]
for i in s:
    result.append([int(i),int(i)])
#print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('LengthOfContent-Length.csv')
csv=pd.read_csv('LengthOfContent-Length.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) 
ax.set_xlabel('LengthOfContent-Length')
ax.set_ylabel('LengthOfContent-Length')
plt.show()


s=['0', '5', '104', '16', '48', '65', '18']
result=[]
for i in s:
    result.append([int(i),int(i)])
print(result)
name=['A1','A2']
CSV=pd.DataFrame(columns=name,data=result)
CSV.to_csv('LengthOfAccept.csv')
csv=pd.read_csv('LengthOfAccept.csv')
#print(csv['A1'])
for i in s:
    result.append([i,i])
#print(result)
fig, ax = plt.subplots()
ax.scatter(csv['A1'], csv['A2']) 
ax.set_xlabel('LengthOfAccept')
ax.set_ylabel('LengthOfAccept')
plt.show()


########################################################################################################################

#Create table of amount

NumberOfKey=[5, 6, 7, 8, 9, 10, 11, 12, 20]
LengthOfRequest=[15, 17, 19, 21, 23, 24, 26, 27, 28, 29, 30, 32, 33, 34, 35, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 89, 90, 91, 92, 93, 95, 96, 99, 101, 104, 105, 106, 108, 109, 110, 114, 115, 116, 118, 119, 120, 121, 122, 126, 127, 129, 130, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147, 148, 150, 151, 152, 153, 155, 158, 159, 160, 162, 168, 169, 170, 171, 174, 175, 176, 177, 178, 179, 180, 182, 187, 190, 191, 192, 194, 195, 198, 200, 201, 204, 207, 208, 212, 213, 217, 218, 220, 222, 224, 227, 228, 229, 231, 232, 233, 234, 235, 237, 239, 240, 241, 242, 245, 249, 250, 258, 266, 267, 268, 269, 283, 289, 290, 310, 330, 337, 338, 340, 354, 372, 378, 387, 400, 414, 647, 722, 754, 761, 846, 921]
NumberOfSlashInRequest=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18]
LengthOfAccept=[0, 5, 16, 18, 48, 65, 104]
LengthOfContentLength=[0, 494, 544, 634, 694, 1861, 2013, 2540, 4243, 5378, 20609]
LengthOfContentType=[0, 12, 18, 26, 35, 88]  

textFile=open('total_http_header.csv','rb')
data= pd.read_csv(textFile)
temp=[NumberOfKey,LengthOfRequest,NumberOfSlashInRequest,LengthOfAccept,LengthOfContentLength,LengthOfContentType]
temp2=['NumberOfKey','LengthOfRequest','NumberOfSlashInRequest','LengthOfAccept','LengthOfContent-Length','LengthOfContent-Type']


def CreatCSV(x,y):
    name=[x,'Value']
    CSV=pd.DataFrame(columns=name,data=y)
    CSV.to_csv(x+'Value.csv')
    return x


def PrintTable(csvFile):
    csv=pd.read_csv(csvFile+'Value.csv')
    plt.plot(csv[csvFile], csv['Value'])
    plt.xlabel("Value Of "+csvFile)
    plt.ylabel("Amount")
    plt.show()

def CreatList(x):
    n=0
    for i in temp2:
        if i == x:
            break
        n+=1
    a=[]
    for i in temp[n]:
       # print(type(i))
        s=0
        for each in data[x]:
          #  print(data[x])
            if i == each:
                s+=1
        a.append([i,s])
    print(a)
    return a
    

for i in temp2:
    newlist=CreatList(i)
    CSV=CreatCSV(i,newlist)
    table=PrintTable(CSV)