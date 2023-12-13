
class tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



#Sample tree

a =tree(3)
b =tree(11)
c =tree(4)
d =tree(4)
e =tree(-2)
f =tree(1)


a.left = b
a.right = c

b.left = d
b.right = e

c.right = f


#time complexity - o(n) 
#space complexity - o(n) 



#depth first - recursive

def treesum(root):
    if root ==None:
        return 0
    
    leftleafs = treesum(root.left)
    rightleafs = treesum(root.right)

    result = root.val+max(leftleafs,rightleafs)
    return result


print(treesum(a))
