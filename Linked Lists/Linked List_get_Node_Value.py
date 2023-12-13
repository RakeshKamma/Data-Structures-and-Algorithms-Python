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
def linked_list_traversal2(head,index,count=0):
       if head is None:
            return head
       if count==index:
            return head.val
       count+=1
       
       return linked_list_traversal2(head.next,index,count)
    

print(linked_list_traversal2(a,15))