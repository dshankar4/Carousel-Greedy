from collections import defaultdict
import time
start_time = time.time()     
def add_node(original,modified,node,feasible):
    xx=set(feasible)
    for i in feasible:
        xx=xx.union(set(original[i]))
    
    modified[node]=[]
    for i in original[node]:
        if i not in xx:
            modified[i]=[]
            for j in original[i]:
                if(j in modified):
                    modified[i].append(j)
                    modified[j].append(i)
        
    return modified    

def del_node(original,node):
    d=defaultdict(list)
    for i in original:
        d[i]=[]
        for j in original[i]:
            d[i].append(j)
    
    xx=d[node]
    del d[node]
    for i in original[node]:
        if(i in d):
            del d[i]
    #print(xx,d)
    for i in xx:
        for j in original[i]:
            if j in d:
                d[j].remove(i)
    return d

def partial_greedy(graph):
    degrees={}
    for i in graph.keys():
        degrees[i]=len(graph[i])
        
    minval=min(degrees.values())
    node=[key for key in degrees if(minval==degrees[key])]
    #print(maxval,node)
    return node[0]

def greedy(graph,result): 
    #print('graph is',graph)
    if(not graph): 
        return [result,graph]
    
    degrees={}
    for i in graph.keys():
        degrees[i]=len(graph[i])
        
    minval=min(degrees.values())
    node=[key for key in degrees if(minval==degrees[key])]
    current=node[0]
    
    d=defaultdict(list)
    for i in graph:
        d[i]=[]
        for j in graph[i]:
            d[i].append(j)
    
    xx=d[current]
    
    del d[current]
    for i in graph[current]:
        if(i in d):
            del d[i]
    #print(xx,d)
    for i in xx:
        for j in graph[i]:
            if j in d:
                d[j].remove(i)
    
    return greedy(d,result+[current])
            

# Driver Code 
"""V = 8

# Defines edges 
E = [ (1, 2), 
	(1, 3), 
	(1, 4), 
	(5, 2), 
	(5, 3),
	(5, 4),
   (5, 6)] 

graph = defaultdict(list) 

for i in range(len(E)): 
    v1, v2 = E[i] 
    graph[v1].append(v2) 
    graph[v2].append(v1)""" 
file=open("frb30-15-mis/frb30-15-mis/frb30-15-1.mis","r")
_,_,V,_=file.readline().split()
V=int(V)
print(V)
E=[]
for line in file:
    line=line.split()
    E.append([int(line[1]),int(line[2])])

graph = defaultdict(list) 

for i in range(len(E)): 
    v1, v2 = E[i] 
    graph[v1].append(v2) 
    graph[v2].append(v1)
#print(graph)
#print(len(greedy(graph,[])[0]))
#mod=del_node(graph,2)
#mod=del_node(mod,3)
#print(mod)
#print(add_node(graph,mod,2))
#print("--- %s seconds ---" % (time.time() - start_time))