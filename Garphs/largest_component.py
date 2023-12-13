


graph ={
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}


def depth_first_search(graph,source,visited):

    if source in visited:return 0
    visited[source]=''
    count=1

    for i in graph[source]:
        count+=depth_first_search(graph,i,visited)

    return count




def large_count(graph):
    visited={}
    max=0
    for i in graph:
        temp=depth_first_search(graph,i,visited)
        if temp>max:
            max = temp
    
    return max


print(large_count(graph))