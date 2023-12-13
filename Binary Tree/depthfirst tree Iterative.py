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


def depthfirst(root):
    if root== None:
        return []
    
    stack = [root]
    result=[]
    while(len(stack)>0):
        current =stack.pop()
        result.append(current.val)

        if current.right!=None: stack.append(current.right)
        if current.left!=None:stack.append(current.left)

    return result

print(depthfirst(a))

