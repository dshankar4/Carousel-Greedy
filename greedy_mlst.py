def del_node(original,modified,label):
    for u,v in original[label]:
        modified[u].remove(v)
        modified[v].remove(u)
    return modified   

def add_node(original,modified,label):
    for u,v in original[label]:
        modified[u].append(v)
        modified[v].append(u)
    return modified

def partial_greedy(label_graph,graph,result):
    V=len(list(graph.keys()))
    count={}
    for i in set(label_graph.keys())-set(result):
        d={}
        for s in graph:
            d[s]=[]
            for j in graph[s]:
                d[s].append(j)
        
        for u,v in label_graph[i]:
            d[u].append(v)
            d[v].append(u)
        
        count[i]=NumberOfconnectedComponents(d,V)
    minval=min(count.values())
    node=[key for key in count if(minval==count[key])][::-1]
    return node[0]

def NumberOfconnectedComponents(graph,V):
    visited =[False]*V
    count = 0
    for v in range(1,V+1):
        if (visited[v-1] == False):
            dfs(v, visited,graph)
            count += 1
    return count
 
def dfs(vertex,visited,graph):
    visited[vertex-1] = True
    for i in graph[vertex]:
        if (not visited[i-1]):
            dfs(i,visited,graph)

def greedy(graph,result,label_graph,V):
    noofcon=NumberOfconnectedComponents(graph,V)
    #print(noofcon,graph)
    if(noofcon==1):
        return[result,graph]
    count={}
    #print(label_graph.keys())
    #print(set(result))
    #print(set(label_graph.keys())-set(result))
    for i in set(label_graph.keys())-set(result):
        #print(i)
        
        d={}
        for s in graph:
            d[s]=[]
            for j in graph[s]:
                d[s].append(j)
        
        for u,v in label_graph[i]:
            d[u].append(v)
            d[v].append(u)
        
        count[i]=NumberOfconnectedComponents(d,V)
        #print('count of no of components on adding on',i,count[i])
    #print(count)
    minval=min(count.values())
    node=[key for key in count if(minval==count[key])][::-1]
    i=node[0]
    for u,v in label_graph[i]:
        graph[u].append(v)
        graph[v].append(u)
    return greedy(graph,result+[i],label_graph,V)

V=7
E = [(4, 7,'c'),
   (1, 2,'a'), 
	(1, 4,'b'),
	(1, 7,'d'), 
	(2, 5,'b'), 
	(2, 3, 'a'),
	(3, 7,'d'),
   (3, 6,'b'),
   (4, 5,'a'),
   (5, 6,'a'),
   (5, 7,'c'),
   (6, 7,'c'),]

graph={}
for i in range(1,V+1):
    graph[i]=[]
label_graph={}
for u,v,l in E:
    if(l not in label_graph):
        label_graph[l]=[]
    label_graph[l].append((u,v))
#print(greedy(graph,[],label_graph,V)[0])    