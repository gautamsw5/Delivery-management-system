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
            nxt=graphColLabel[graph[delidx].index(temp)]
            approxroute.append(nxt)
        del graph[delidx]
        del graphRowLabel[delidx]
        curr=nxt
    return approxroute,approxdist



graph1=[]
graphcpy=[]
n=int(input("Enter number of delivery points: "))
print("Enter the graph (",n," distances in a line)")
for i in range(n):
    graph1.append(list(map(int,input().split())))
    graphcpy.append(list(graph1[i]))
