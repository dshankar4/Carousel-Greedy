from collections import defaultdict
from math import ceil
from greedy_mlst import *
def cg(label_graph,alpha,beta,V):
    graph={}
    for i in range(1,V+1):
        graph[i]=[]
    
    feasible,modified=greedy(graph,[],label_graph,V)
    #print(feasible)
    s=len(feasible)
    print(s)
    #print(feasible)
    remove=ceil(beta*s)
    for i in range(1,remove+1):
        modified=del_node(label_graph,modified,feasible[-i])
    if(remove>0):
        feasible=feasible[:-remove]
    n=alpha*s
    for i in range(n):
        #print()
        #print('iteration :',i)
        #print('feasible vector: ',feasible)
        remove=feasible.pop(0)
        #print('removed item',remove,' existing graph',modified)
        modified=del_node(label_graph,modified,remove)
        #print('after removing ',modified)
        #modi_gra=partial_soln(graph,feasible)
        #print(modi_gra,feasible)
        #print(feasible,modi_gra,greedy(modi_gra))
        x=partial_greedy(label_graph,modified,feasible)
        #print('output of greedy',x)
        modified=add_node(label_graph,modified,x)
        #print("after adding to feasible ",modified)
        feasible+=[x]
    #print(feasible)
    #print(modified)
    feasible=greedy(modified,feasible,label_graph,V)[0]
    return feasible
"""
V=7
E = [ (1, 2,'a'), 
	(1, 4,'b'),
   (1, 7,'d'),
   (4, 7,'c'),
   (2, 5,'b'), 
	(2, 3, 'a'),
	(3, 7,'d'),
   (3, 6,'b'),
   (4, 5,'a'),
   (5, 6,'a'),
   (5, 7,'c'),
   (6, 7,'c'),]

label_graph={}
for u,v,l in E:
    if(l not in label_graph):
        label_graph[l]=[]
    label_graph[l].append((u,v))
"""
file=open("frb30-15-mis/frb30-15-mis/frb30-15-5.mis","r")
_,_,V,_=file.readline().split()
V=int(V)
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
#print(cg(graph,2,0))
print(cg(graph,1,0.3,V))