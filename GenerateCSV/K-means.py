#K-means.py
NumberOfKey=[7, 8, 9, 6, 11, 10, 20, 5, 12]
point1=[7,12,20]
LengthOfRequest=[78, 74, 72, 73, 66, 69, 32, 65, 75, 48, 49, 52, 33, 61, 84, 30, 44, 40, 43, 54, 51, 63, 50, 38, 122, 217, 180, 82, 64, 34, 121, 289, 127, 187, 207, 19, 220, 310, 340, 62, 21, 41, 58, 99, 29, 26, 46, 231, 77, 55, 53, 177, 235, 37, 86, 24, 17, 71, 70, 80, 76, 90, 59, 47, 57, 68, 67, 42, 198, 171, 176, 175, 283, 135, 79, 27, 152, 60, 153, 159, 150, 290, 56, 104, 387, 378, 45, 101, 87, 143, 169, 266, 91, 233, 158, 195, 81, 921, 846, 137, 116, 174, 132, 144, 146, 96, 108, 106, 133, 83, 93, 120, 178, 761, 754, 722, 647, 372, 337, 136, 192, 400, 142, 141, 140, 139, 138, 119, 35, 338, 15, 204, 414, 354, 23, 126, 330, 129, 218, 222, 162, 130, 95, 118, 228, 267, 240, 148, 213, 268, 234, 200, 134, 250, 182, 115, 89, 114, 160, 224, 212, 190, 170, 269, 105, 232, 155, 168, 229, 201, 191, 239, 208, 110, 227, 242, 245, 194, 237, 258, 249, 92, 151, 147, 241, 109, 179, 28]
point2=[200,400,800]
NumberOfSlashInRequest=[10, 6, 7, 8, 3, 4, 5, 2, 1, 9, 18, 13, 14, 12, 11, 15]
point3=[5,12,18]
LengthOfAccept=[5, 104, 16, 48, 65, 0, 18]
point4=[20,50,100]
LengthOfContentLength=[0, 2013, 4243, 2540, 694, 5378, 544, 20609, 634, 1861, 494]
point5=[2500,5000,20000]
LengthOfContentType=[0, 35, 26, 88, 18, 12]
point6=[15,40,80]
import math
def CalFirstGroup(point,Class):    

    s=[]
    for each in Class:
        a=[]
        for i in point:
            temp=math.fabs(i-each)
            a.append(temp)
       # print(a)
        max_num = a[0]
        min_num = a[0]
        max_index = 0
        min_index = 0
        for i in range(len(a)):
            if a[i]>max_num:
                max_num = a[i]
                max_index = i
            else:
                min_num = a[i]
                min_index = i
        
        s.append(min_index)
    return s,Class,point

def DivideClass(s,Class,point):
    result=[]
    for i in range(len(point)):
        c=[]
        c.append(point[i])
        n=0
        for each in s:
            if each == i:
                c.append(Class[n])
            n+=1
        result.append(c)
    return(result)
  
def Cluster(result):
    temp=[]
    for i in result:
        total=0
        for each in range(len(i)):
            total = total + i[each]
        newpoint=total/(len(i))
        temp.append(newpoint)
    return temp

##############################################################
#Calculate NumberOfKey
print("Calculate NumberOfKey")
a=CalFirstGroup(point1,NumberOfKey)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,NumberOfKey)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1

##############################################################
#Calculate LengthOfRequest 
print("Calculate LengthOfRequest")
a=CalFirstGroup(point2,LengthOfRequest)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,LengthOfRequest)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1
    
##############################################################
#Calculate NumberOfSlashInRequest 
print("Calculate NumberOfSlashInRequest")
a=CalFirstGroup(point3,NumberOfSlashInRequest)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,NumberOfSlashInRequest)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1
    
##############################################################
#Calculate LengthOfAccept 
print("Calculate LengthOfAccept")
a=CalFirstGroup(point4,LengthOfAccept)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,LengthOfAccept)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1
    
##############################################################
#Calculate LengthOfContentLength 
print("Calculate LengthOfContentLength")
a=CalFirstGroup(point5,LengthOfContentLength)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,LengthOfContentLength)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1
##############################################################
#Calculate LengthOfContentType 
print("Calculate LengthOfContentType")
a=CalFirstGroup(point6,LengthOfContentType)
b=DivideClass(a[0],a[1],a[2])
c=Cluster(b)
n=0
while n<5:
    a=CalFirstGroup(c,LengthOfContentType)
    b=DivideClass(a[0],a[1],a[2])
    c=Cluster(b)
    print(c)
    n+=1

###############################################################
#breakpoint.py
print("breakpoint:")
NumberOfKey=[7,11,20]
LengthOfRequest=[89,246,775]
NumberOfSlashInRequest=[3,6,12]
LengthOfAccept=[10,48,73]
LengthOfContentLength=[1098,4811,20599]
LengthOfContentType=[10,30,88]
t=[NumberOfKey,LengthOfRequest,NumberOfSlashInRequest,LengthOfAccept,LengthOfContentLength,LengthOfContentType]
breakpoint=[]
for i in t:

    bp1=(i[0]+i[1])/2
    bp2=(i[1]+i[2])/2
    breakpoint.append([bp1,bp2])
print(breakpoint)