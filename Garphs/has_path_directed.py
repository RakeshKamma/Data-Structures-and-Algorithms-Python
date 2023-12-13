#n - no of nodes
#e - no of edges

#time complexity - o(e)
#space complexity - o(n)

#or anything is fine

#n - no of nodes
#e - n^2 max edges

#time complexity - o(n^2)
#space complexity - o(n)

graph ={
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]

}

#depth first search- recursive


def has_path(graph,source,target):
    if source == target: return True 
    #if graph[source]==[]: return False

    for i in graph[source]:
        if (has_path(graph,i,target)) == True:
            return True
    
    return False



print(has_path(graph,'f','h'))


#breath_first - iterative
def has_path_breath(graph,source,target):
    queue=[source]

    while(len(queue)>0):
        current = queue.pop(0)
        if current == target: return True
        for i in graph[current]:
            queue.append(i)

    return False


print(has_path_breath(graph,'f','h'))

