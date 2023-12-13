graph ={
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]

}

#n- no of nodes

#time complexity O(n^2)
#space complexity o(n)

#depth first -iterative

def depth_first_iterative(graph,source):
    stack=[source]
    result=[]
    while(len(stack)>0):
        current = stack.pop()
        result.append(current)
        for  i in graph[current]:
            stack.append(i)

    return result


print(depth_first_iterative(graph,'a'))


# depth first - Recursive

def depth_first_recursive(graph,source):
    if graph[source]==[]: return [source]
    result=[]
    for i in graph[source]:
        result.extend(depth_first_recursive(graph,i))

    result.insert(0,source)

    return result


print(depth_first_recursive(graph,'a'))




#n- no of nodes

#time complexity O(n^2)
#space complexity o(n)

# breath first - iterative

def breathfirst(graph,source):
    queue=[source]
    result=[]
    while(len(queue)>0):
        current = queue.pop(0)
        result.append(current)
        for i in graph[current]:
            queue.append(i)

    return result




print(breathfirst(graph,'a'))