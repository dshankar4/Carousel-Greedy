from collections import defaultdict
import time
start_time = time.time()     
def add_node(original,modified,node):
    modified[node]=[]
    for i in original[node]:
        if(i in modified):
            modified[node].append(i)
            modified[i].append(node)
    
    return modified
        
def del_node(original,node):
    d=defaultdict(list)
    for i in original:
        d[i]=[]
        for j in original[i]:
            d[i].append(j)
    
    del d[node]
    for i in original[node]:
        if i in d:
            d[i].remove(node)

    return d

def greedy(graph,result): 
    #print(graph)
    if(all([i==[] for i in graph.values()])):
       return [result,graph]   
    
    degrees={}
    for i in graph.keys():
        degrees[i]=len(graph[i])
    maxval=max(degrees.values())
    node=[key for key in degrees if(maxval==degrees[key])]
    #print(maxval,node)
    current=node[0]
    
    d=defaultdict(list)
    for i in graph:
        d[i]=[]
        for j in graph[i]:
            d[i].append(j)
    
    #print(d)
    del d[current]
    for i in graph[current]:
        if i in d:
            d[i].remove(current)
        #print(d,graph)
    #print('this graph',graph)
    return greedy(d,result+[current])
            
def partial_greedy(graph):
    degrees={}
    for i in graph.keys():
        degrees[i]=len(graph[i])
        
    maxval=max(degrees.values())
    node=[key for key in degrees if(maxval==degrees[key])]
    #print(maxval,node)
    return node[0]

# Driver Code 
file=open("frb30-15-mis/frb30-15-mis/frb30-15-1.mis","r")
_,_,V,_=file.readline().split()
V=int(V)
print(V)
E=[]
for line in file:
    line=line.split()
    E.append([int(line[1]),int(line[2])])
'''V = 8

E = [ (1, 2), 
	(1, 3), 
	(1, 4), 
	(5, 2), 
	(5, 3),
	(5, 4)]'''


graph = defaultdict(list)
for i in range(len(E)): 
    v1, v2 = E[i] 
    graph[v1].append(v2) 
    graph[v2].append(v1)

print(len(greedy(graph,[])[0]))
#print(graph)
#print("--- %s seconds ---" % (time.time() - start_time))