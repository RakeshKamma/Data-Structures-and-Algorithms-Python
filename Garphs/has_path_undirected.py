edges = [
['i','j'],
['k','i'],
['m','k'],
['k','l'],
['o','n'],

]

#example
# graph ={
#     'i':['j','k'],
#     'j':['i'],
#     'k':['i','m','l'],
#     'm':['k'],
#     'l':['k'],
#     'o':['n'],
#     'n':['o']

# }

graph={}

#approach-1 - inefficient

# for a in edges:
#     for b in a:
#         temp =a.copy()
#         temp.remove(b)
#         if b not in graph:
#             graph[b] =temp
#         else:
#             graph[b].extend(temp)


#approach-2 - efficient
for i in edges:
    a,b =i
    if a not in graph: graph[a]=[]
    if b not in graph: graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)

print(graph)


#faster access of data values - use dictinary or keys


#depth first search- recursive
def has_path(graph,source,target,visited=set()):
    if source == target: return True 
    
    # no need of this line as there is a return False at the end
    # if graph[source]==[]: return False

    if source in visited: return False
    visited.add(source)

    for i in graph[source]:
        if (has_path(graph,i,target,visited)) == True:
            return True
    
    return False


print(has_path(graph,'o','i'))