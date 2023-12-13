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


def linked_list_traversal1(head):
    current=head
    result=[]
    while(current is not None):
        result.append(current.val)
        current=current.next
    
    return result

print(linked_list_traversal1(a))


#recursive
def linked_list_traversal2(head):
    current = head
    result=[]
    if current is None:
        return []
    temp =linked_list_traversal2(current.next)
    result.extend(current.val)
    result.extend(temp)

    return result



print(linked_list_traversal2(a))