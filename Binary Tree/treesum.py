
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


#n- no of nodes

#time complexity - o(n) 
#space complexity - o(n) 

#depth first - recursive

def treesum(root):
    if root ==None:
        return 0
    
    leftleafs = treesum(root.left)
    rightleafs = treesum(root.right)

    result = root.val+ leftleafs + rightleafs
    return result

print(treesum(a))


#breathfirst - iterative

def treesum_breathfirst(root):
    if root==None: return 0

    queue=[root]
    result=0
    while(len(queue)>0):
        current= queue.pop(0)
        result+=current.val
        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)
    
    return result
print(treesum_breathfirst(a))

