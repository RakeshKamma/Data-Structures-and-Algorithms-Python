import queue


class tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



#Sample tree

a =tree('a')
b =tree('b')
c =tree('c')
d =tree('d')
e =tree('e')
f =tree('f')


a.left = b
a.right = c

b.left = d
b.right = e

c.right = f


#n- no of nodes

#time complexity - o(n) 
#space complexity - o(n) 


#breathfirst - iterative

def breathfirst(root,target):
    if root==None: return []

    queue=[root]

    while(len(queue)>0):
        current= queue.pop(0)
        if current.val == target: return True
        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)
    
    return False
print(breathfirst(a,''))
print(breathfirst(a,'f'))
print(breathfirst(a,'g'))


# depth first - recursive

def depthfirst(root,target):
    if root ==None: return False
    if root.val == target:return True
    

    leftvalues  = depthfirst(root.left,target)
    rightvalues = depthfirst(root.right,target)

    result = leftvalues or rightvalues

    return result
print(depthfirst(a,''))
print(depthfirst(a,'f'))
print(depthfirst(a,'g'))
