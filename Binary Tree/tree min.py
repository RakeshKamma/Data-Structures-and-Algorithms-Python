
class tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



#Sample tree

a =tree(5)
b =tree(11)
c =tree(3)
d =tree(4)
e =tree(15)
f =tree(12)


a.left = b
a.right = c

b.left = d
b.right = e

c.right = f


#n- no of nodes

#time complexity - o(n) 
#space complexity - o(n) 



#depth first - recursive

def treesum(root):
    if root ==None:
        return 10000000000
    
    leftleafs = treesum(root.left)
    rightleafs = treesum(root.right)

    result = min(root.val,leftleafs,rightleafs)

    return result

print(treesum(a))