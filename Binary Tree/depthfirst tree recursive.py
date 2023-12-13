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
    if root ==None:
        return []
    leftleafs = depthfirst(root.left)
    rightleafs = depthfirst(root.right)

    result = [root.val]
    result.extend(leftleafs)
    result.extend(rightleafs)
    return result

print(depthfirst(a))


        

