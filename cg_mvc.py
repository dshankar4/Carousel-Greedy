import time
from collections import defaultdict
from math import ceil
from greedy_mvc import *
start_time = time.time()
def cg(graph,alpha,beta):
    feasible,modified=greedy(graph,[])
    #print(feasible)
    s=len(feasible)
    #print(s)
    #print(feasible)
    remove=ceil(beta*s)
    for i in range(1,remove+1):
        modified=add_node(graph,modified,feasible[-i])
    if(remove>0):
        feasible=feasible[:-remove]
    n=alpha*s
    for i in range(n):
        #print()
        #print('iteration :',i)
        #print('feasible vector: ',feasible)
        remove=feasible.pop(0)
        #print('removed item',remove,' existing graph',modified)
        modified=add_node(graph,modified,remove)
        #print('after removing ',modified)
        #print(feasible,graph)
        #modi_gra=partial_soln(graph,feasible)
        #print(modi_gra,feasible)
        #print(feasible,modi_gra,greedy(modi_gra))
        x=partial_greedy(modified)
        #print('output of greedy',x)
        modified=del_node(modified,x)
        #print("after adding to feasible ",modified)
        feasible+=[x]
        
    feasible+=greedy(modified,[])[0]
    return feasible

"""V = 8

# Defines edges 
E = [ (1, 2), 
	(1, 3), 
	(1, 4), 
	(5, 2), 
	(5, 3),
	(5, 4),
   (5, 6)]"""
file=open("frb30-15-mis/frb30-15-mis/frb30-15-1.mis","r")
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
print(len(cg(graph,20,0.01)))
print("--- %s seconds ---" % (time.time() - start_time))