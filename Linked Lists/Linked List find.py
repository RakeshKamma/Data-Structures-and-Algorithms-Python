class Node:
    def __init__(self,val):
        self.val= val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next =b
b.next =c
c.next =d


#recursive
def linked_list_traversal2(head,target):
    current = head
    if current is None:
        return False
    if current.val == target:
        return True
    return linked_list_traversal2(current.next,target)
       
    

print(linked_list_traversal2(a,'G'))