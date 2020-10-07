import math

def distance(a,b,c,d):                             #Function to find distance between points (a,b) and (c,d)
    return math.sqrt((a-c)**2+(b-d)**2)

def angle(X,Y,a,b):
    x=X-a
    y=Y-b
    if x==0 and y>0:
        return math.pi/2
    if x==0 and y<0:
        return 3*math.pi/2
    if y==0 and x<0:
        return math.pi
    if y==0 and x>0:
        return 0
    if x>0 and y>0:
        return math.atan(y/x)
    if x<0 and y>0:
        return math.pi+math.atan(y/x)
    if x<0 and y<0:
        return math.pi+math.atan(y/x)
    if x>0 and y<0:
        return 2*math.pi+math.atan(y/x)
    return 0
# Approximate method using mergesort on polar coordinates by taking start point as origin
def merge(l,r,dell,delr,px,py):
    i=0
    j=0
    x=[]
    delp=[]
    while i<len(l) or j<len(r):
        if i<len(l) and j<len(r):
            if l[i]<r[j]:
                x.append(l[i])
                delp.append(dell[i])
                i=i+1
            elif l[i]>r[j]:
                x.append(r[j])
                delp.append(delr[j])
                j=j+1
            elif l[i]==r[j]:
                pp=[px,py]
                if delp!=[]:
                    pp=delp[len(delp)-1]
                if distance(pp[0],pp[1],dell[i][0],dell[i][1])<=distance(pp[0],pp[1],delr[j][0],delr[j][1]):
                    x.append(l[i])
                    delp.append(dell[i])
                    i=i+1
                else:
                    x.append(r[j])
                    delp.append(delr[j])
                    j=j+1
        elif i>=len(l) and j<len(r):
            x.append(r[j])
            delp.append(delr[j])
            j=j+1
        elif i<len(l) and j>=len(r):
            x.append(l[i])
            delp.append(dell[i])
            i=i+1
    return x,delp
def mergesort(a,delivpts,px,py):
    ln=len(a)
    if ln>1:
        q=ln//2
        l=a[:q]
        r=a[q:]
        dell=delivpts[:q]
        delr=delivpts[q:]
        temp=mergesort(l,dell,px,py)
        l=temp[0]
        dell=temp[1]
        temp=mergesort(r,delr,px,py)
        r=temp[0]
        delr=temp[1]
        temp=merge(l,r,dell,delr,px,py)
        a=temp[0]
        delivpts=temp[1]
    return a,delivpts

def anglesort(delivpts,a,b):
    angles=[]
    for i in delivpts:
        angles.append(angle(i[0],i[1],a,b))
    return mergesort(angles,delivpts,a,b)

delivpts=[]   #List to store order delivery coordinates         #(input)
print("Enter the pickup coordinates (separated by space) : ")
a,b=map(int,input().split())
while True:
    print("Enter coordinates (in meters) of delivery : ")
    temp1=input()
    if temp1=="OK" or temp1=="Ok" or temp1=="ok" or temp1=="oK":
        break
    temp1,temp2=map(int,temp1.split())
    delivpts.append([temp1,temp2])

#Sample inputs
#a,b=0,0
#delivpts=[[0.5,1],[3,3],[2,3]]
#delivpts=[[3,3],[2,3],[0.5,1],[11,13],[11,14],[11,15],[11,16],[11,17],[11,18]]
#delivpts=[[0.5,1],[3,3],[1,1],[2,2]]
#delivpts=[[0.5,1],[3,0],[1,4],[4,4],[2,1]]
#End of Sample inputs

delivptscpy=[i for i in delivpts]         #Create copy of original delivery coordinates (can be used if order details also need to be displayed
i=0
while i<len(delivpts)-1:                  #Delete repeated delivery coordinates to optimize the algorithms reducing n value and hence
                                          #reduce the time consumed                 
    j=i+1
    while j<len(delivpts):
        if delivpts[i]==delivpts[j]:
            del delivpts[i]
            i=i-1
            continue
        j=j+1
    i=i+1
n=len(delivpts)
m=int(input("Enter number of delivery boys/trucks : "))
angles,delivpts=anglesort(delivpts,a,b)
c=0
delivptsdiv=[[] for i in range(m)]
i=1
delivptsdiv[0].append(delivpts[0])
while c<m and i<n:
    if angles[i]==angles[i-1] or i<(c+1)*n//m:
        delivptsdiv[c].append(delivpts[i])
        i=i+1
    else:
        c=c+1
f=0
i=0
while i<len(delivptsdiv):
    if len(delivptsdiv[i])==0:
        f=1
        c=c-1
        del delivptsdiv[i]
        i=i-1
    i=i+1
if f==1:
    print("You need only ",len(delivptsdiv)," delivery boys/trucks for this set of deliveries.")
print(delivptsdiv)
