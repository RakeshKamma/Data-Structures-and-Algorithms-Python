edges=[
    ['a','c'],
    ['a','b'],
    ['c','b'],
    ['c','d'],
    ['b','d'],
    ['e','d'],
    ['g','f'],
]

graph={}

for i in edges:
    a,b=i
    if a not in graph: graph[a]=[]
    if b not in graph: graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)

print(graph)


#depth first -recursive
# def shortest_path(graph,source,target,visited={}):
#     if source == target : return 0
#     if source in visited: return 0
#     visited[source]=""
#     count=1
#     for i in graph[source]:
#         count+=shortest_path(graph,i,target)

#     return count

# print(shortest_path(graph,'w','x'))


#breath first -queue

def shortest_path_1(graph,source,target,visited={}):
    queue=[(source,0)]

    while(len(queue)>0):
        current = queue.pop(0)

        if current[0] not in visited: visited[current[0]]=''
        else: continue 

        if current[0] == target: return current[1]
        for i in graph[current[0]]:
            queue.append((i,current[1]+1))
    
    return -1

print(shortest_path_1(graph,'b','g'))



#breath first -queue

def shortest_path_2(graph,source,target,visited={}):
    queue=[(source,0)]
    visited[source]=''

    while(len(queue)>0):
        current = queue.pop(0)

        if current[0] == target: return current[1]
        for i in graph[current[0]]:
            if current[0] not in visited: 
                visited[current[0]]='' 
                queue.append((i,current[1]+1))
    
    return -1

print(shortest_path_2(graph,'b','g'))