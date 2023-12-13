graph ={
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

#depth first recursive
def connected_components_count(graph,source,visited):
    if source in visited:
        return False
    visited[source]=''
            
    for i in graph[source]:
        connected_components_count(graph,i,visited)

    return True




def find_count(graph):
    visited={}
    count=0
    for i in graph:
       if connected_components_count(graph,i,visited) == True:
           count+=1

    return count
        

    
    

print(find_count(graph))