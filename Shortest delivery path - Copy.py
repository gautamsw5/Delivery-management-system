import math

def distance(a,b,c,d):
    return math.sqrt((a-c)**2+(b-d)**2)

def pointsToGraph(delivpts,a,b):
    delivpts=[[a,b]]+delivpts
    graph=[]                                       # 2-D list to store distances between all pairs of points #Graph DS
    for i in range(0,len(delivpts)):
        graph.append([])
        for j in range(0,len(delivpts)):
            graph[i].append(distance(delivpts[i][0],delivpts[i][1],delivpts[j][0],delivpts[j][1]))
    return graph

#Backtracking to find minimum possible distance of a travelling salesman problem (which is different from our problem statement)
#that can cover all points (to confirm the answer (approximately))
#but does not work on values of n more than 9
answer=[]
routes=[]     #List to store all possible routes
distances=[]  #List to store distances of above routes
def tsp(graph,v,currPos,n,count,cost):        #Recursive function to find minimum distance
    if count==n and graph[currPos][0]:        #If last point is reached then append to the total distance
        answer.append(cost)
        return                                #Return to check for minimum answer  
    for i in range(n):                        #Loop to traverse the boolean list
        if v[i]==False and graph[currPos][i]:
            v[i]=True                         #Mark as visited
            tsp(graph,v,i,n,count+1,cost+graph[currPos][i]) #Backtracking step of currPos and increasing the count by 1
                                                            #and cost by graph[currPos][i] value
            v[i]=False                        #Mark i th point as unvisited
def backtrack(delivpts,a,b):                              #Function to Call the tsp function
    graph=pointsToGraph(delivpts,a,b)[0]
    n=len(graph) 
    v=[False for i in range(n)]               #Boolean list to check if a point has been visited or not 
    v[0]=True                                 #Mark start point as visited
    tsp(graph,v,0,n,1,0)                       #Find the minimum weight Cycle
    print(min(answer))                        #answer is the minimum distance in which all points can be covered

#Brute Force Method #Does not work on values of n more than 8 to find best route as well as minimum distance
def permutation(lst):                         #Function to find all permutations of a given list using Divide and Conquer
    if len(lst)<=1:
        return [lst]
    l=[]                                      #List that will store current permutation  
    for i in range(len(lst)): 
        m=lst[i]                              #Extract lst[i] as m from the list
        remLst=lst[:i]+lst[i+1:]              #remLst is remaining list
        for p in permutation(remLst):         #Generating all permutations in which m is first element
            l.append([m]+p)
    return l
def bforce(delivpts,a,b):                         #Brute Force Function to check all routes
    distances=[]
    routes=permutation(delivpts)          #Exclude start point while taking permutations
    for i in range(len(routes)):              #Go through all permutations
        d=distance(routes[i][0][0],routes[i][0][1],a,b) #Distance between restaurant and first point of current permutation
        for j in range(len(routes[i])-1):
            d+=distance(routes[i][j][0],routes[i][j][1],routes[i][j+1][0],routes[i][j+1][1]) #Distance between consecutive
                                                                                             #points of current permutation
            if i>0 and d>min(distances):
                break
        distances.append(d)
    finalroute=[[0,0]]+routes[distances.index(min(distances))]
    mindist=min(distances)
    return finalroute,mindist

#Approximate method used for higher n values
def nearest(p,l):                           #Function to find point in list l which is at minimum distance from point p
    d=distance(p[0],p[1],l[0][0],l[0][1])   #Store the first distance
    np=l[0]                                 #Store the first point
    for i in range(0,len(l)):
        if d>distance(p[0],p[1],l[i][0],l[i][1]):
            d=distance(p[0],p[1],l[i][0],l[i][1])   #Store the nearest distance
            np=l[i]                         #Store the nearest point
    return np,d
def approxans(delivpts,a,b):
    route=[[a,b]]
    temp=nearest([a,b],delivpts)
    npt=temp[0]
    dist=temp[1]
    while len(delivpts)>1:
        del delivpts[delivpts.index(npt)]
        route.append(npt)
        temp=nearest(npt,delivpts)
        npt=temp[0]
        dist+=temp[1]
    route.append(delivpts[0])
    return route,dist

def Optimization1(route,d):                     #Function that checks whether placing the last point as the second point causes
                                                #any improvement and returns accordingly
    newroute=[route[0]]+[route[-1]]+route[1:-1]
    newd=0
    for i in range(0,len(route)-1):
        newd+=distance(newroute[i][0],newroute[i][1],newroute[i+1][0],newroute[i+1][1])
        if newd>d:
            break
    if newd<=d:
        return newroute,newd
    return route,d

def Optimization2(route,d):
    for i in range(0,len(route)-1):
        
#Approximate Method for graph input
def approxansgraphinput(graph,start):
    approxdist=0
    graphRowLabel=[[j for i in range(0,len(graph))] for j in range(0,len(graph))] # 2-D list to label the graph points row wise
    graphColLabel=[[i for i in range(0,len(graph))] for j in range(0,len(graph))] # 2-D list to label the graph points column wise
    approxroute=[start]
    while len(graph)>0:
        delidx=graphColLabel[0].index(start)
        #print(approxroute,approxdist)
        for i in range(len(graph)):
            del graph[i][delidx]
            del graphColLabel[i][delidx]
            del graphRowLabel[i][delidx]
        if len(graph[delidx])>0:
            temp=min(graph[delidx])
            approxdist+=temp
            start=graphColLabel[0][graph[delidx].index(temp)]
            approxroute.append(start)
        del graph[delidx]
    return approxroute,approxdist

delivpts=[]   #List to store order delivery coordinates         #(input)
customer=[]   #List to store customer name and contact number   #(input)
order=[]      #List to store orders                             #(input)
amt=[]        #List to store order price                        #(input)
print("Enter the restaurant coordinates (separated by space) : ")
a,b=map(int,input().split())
print("Enter orders that are ready : ")
while True:
    print("Enter customer name and mobile number separeted by space : ")
    temp1=input()
    if temp1=="OK" or temp1=="Ok" or temp1=="ok":
        break
    customer.append(temp1)
    print("Enter order name : ")
    order.append(input())
    print("Enter order cost : ")
    amt.append(input())
    print("Enter coordinates (in meters) of delivery : ")
    temp1=input()
    temp1,temp2=map(int,temp1.split())
    delivpts.append([temp1,temp2])

#Sample inputs
customer=["A 73637737","B 83788363","C 97283763"]
order=["a","b","c"]
amt=["10","20","30"]
a,b=0,0
delivpts=[[0.5,1],[3,3],[2,3]]
delivpts=[[3,3],[2,3],[0.5,1],[11,13],[11,14],[11,15],[11,16],[11,17]]
#delivpts=[[0.5,1],[3,3],[1,1],[2,2]]
#delivpts=[[0.5,1],[3,0],[1,4],[4,4],[2,1]]
#End of Sample inputs

delivptscpy=[i for i in delivpts]         #Create copy of original delivery coordinates
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


