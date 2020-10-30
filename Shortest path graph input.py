def permutation(lst):                         #Function to find all permutations of a given list
    if len(lst)<=1:
        return [lst]
    l=[]                                      #List to store all permutations  
    for i in range(len(lst)): 
        m=lst[i]                              #Extract lst[i] as m from the list
        remLst=lst[:i]+lst[i+1:]              #remLst is remaining list
        for p in permutation(remLst):         #Generating all permutations in which m is first element
            l.append([m]+p)
    return l


#Function to get distance of a path on a graph(Adjacency Matrix form)
def getDistance(graph,path):
    dist=0
    for i in range(0,len(path)-1):
        dist+=graph[path[i]][path[i+1]]
    return dist



#Brute Force on graph
def bforcegraph(graph):
    paths=permutation(list(range(1,len(graph))))
    m=getDistance(graph,[0]+paths[0])
    path=[0]+paths[0]
    for i in range(1,len(paths)):
        d=getDistance(graph,[0]+paths[i])
        if(m>d):
            m=d
            path=[0]+paths[i]
    return path,m


#Approximate Method (Greedy Algorithm) for graph input
def approxansgraphinput(graph):
    approxdist=0
    graphRowLabel=[i for i in range(0,len(graph))] # List to label the vertices of the graph (representing labels for rows)
    graphColLabel=[i for i in range(0,len(graph))] # List to label the vertices of the graph (representing labels for columns)
    approxroute=[0]
    curr=0
    while len(graph)>0:
        delidx=graphColLabel.index(curr)
        #print(approxroute,approxdist)
        for i in range(len(graph)):
            del graph[i][delidx]
        del graphColLabel[delidx]
        if len(graph[delidx])>0:
            temp=min(graph[delidx])
            approxdist+=temp
            #print(temp,delidx)
            nxt=graphColLabel[graph[delidx].index(temp)]
            approxroute.append(nxt)
        del graph[delidx]
        del graphRowLabel[delidx]
        curr=nxt
    return approxroute,approxdist


def Optimization1(graph,path,dist):
    newpath=path[0:1]+path[-1:]+path[1:-1]
    newdist=getDistance(graph,newpath)
    if(newdist<dist):
        return newpath,newdist
    return path,dist


def Optimization2(graph,path,dist):
    for i in range(3,len(path)-1):
        newpath=[path[0]]+[path[i]]+path[1:i]+path[i+1:]
        newdist=getDistance(graph,newpath)
        if(newdist<dist):
            path=newpath
            dist=newdist
    return path,dist


def Optimization3(graph,path,dist):
    for i in range(1,len(path)-1):
        for j in range(i+1,len(path)):
            newpath=path[:i]+path[j:j+1]+path[i+1:j]+path[i:i+1]+path[j+1:]
            newdist=getDistance(graph,newpath)
            if(newdist<dist):
                path=newpath
                dist=newdist
    return path,dist


def Optimization(graph,path,dist,n):
    c=40000//n
    i=0
    while i<=c:
        path1,dist1=list(Optimization1(graph,path,dist))
        if path1==path:
            break
        else:
            path=list(path1)
            dist=dist1
        i=i+1
    c=40000//(n**2)
    i=0
    while i<=c:
        path1,dist1=list(Optimization2(path,dist))
        path1,dist1=list(Optimization1(path1,dist1))
        if path1==path:
            break
        else:
            path=list(path1)
            dist=dist1
        i=i+1
    c=40000//(n**3)
    i=0
    while i<c:
        path1,dist1=list(Optimization3(path,dist))
        path1,dist1=list(Optimization2(path1,dist1))
        path1,dist1=list(Optimization1(path1,dist1))
        if path1==path:
            break
        else:
            path=list(path1)
            dist=dist1
        i=i+1
    return path,dist


def ShortestPath(graph,n):
    if n<9:
        return bforcegraph(graph)
    else:
        path,dist=list(approxansgraphinput(graph))
        path,dist=list(Optimization(graph,path,dist,n))
    return path,dist


graph1=[]
graphcpy=[]
n=int(input("Enter number of delivery points: "))
print("Start point is point 0")
for i in range(0,n+1):
    graph1.append([0 for k in range(0,n+1)])
    graphcpy.append([0 for k in range(0,n+1)])
    for j in range(0,n+1):
        if(i!=j):
            print("Enter distance from point",i,"to point",j)
            d=int(input())
            graph1[i][j]=d
            graphcpy[i][j]=d
print("Adjacency matrix:")
for i in graph1:
    print(i)
temp=ShortestPath(graph1,n)
path=temp[0]
dist=temp[1]
print("Optimal path: ",path)
print("Corresponding optimal distance: ",dist)
'''print("Enter the graph (",n," distances in a line)")
for i in range(n):
    graph1.append(list(map(int,input().split())))
    graphcpy.append(list(graph1[i]))'''
