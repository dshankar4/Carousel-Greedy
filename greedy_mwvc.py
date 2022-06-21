from collections import defaultdict

def partial_greedy(graph,weights):
    degrees={}
    for i in graph.keys():
        degrees[i]=weights[i-1]/len(graph[i])
        
    minval=min(degrees.values())
    node=[key for key in degrees if(minval==degrees[key])]
    #print(maxval,node)
    return node[0]

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

def greedy(graph,result,weights): 
    if(all([i==[] for i in graph.values()])):
       return [result,graph]   
	
    degrees={}
    for i in graph.keys():
        degrees[i]=weights[i-1]/len(graph[i])
        
    minval=min(degrees.values())
    node=[key for key in degrees if(minval==degrees[key])]
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
    
    return greedy(d,result+[current],weights)
            

# Driver Code 
V = 8

# Defines edges 
E = [ (1, 2), 
	(1, 3), 
	(1, 4), 
	(5, 2), 
	(5, 3),
	(5, 4)] 

graph = defaultdict(list) 

for i in range(len(E)): 
    v1, v2 = E[i] 
    graph[v1].append(v2) 
    graph[v2].append(v1) 
    

vertex_wei=[1,2,2,1,1]

print(greedy(graph,[],vertex_wei)) 