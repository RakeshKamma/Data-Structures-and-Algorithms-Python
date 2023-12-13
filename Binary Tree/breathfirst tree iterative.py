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
        

def breathfirst(root):
    if root is None:
        return []
    
    queue=[root]
    result=[]

    while(len(queue)>0):

        current = queue.pop(0)
        result.append(current.val)

        if current.left is not None:queue.append(current.left)
        if current.right is not None:queue.append(current.right)

    return result



print(breathfirst(a))