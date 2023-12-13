class Node:
    def __init__(self,val):
        self.val= val
        self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next =b
b.next =c
c.next =d

#recursive
def linked_list_traversal2(head):
    current = head
    result=0
    if current is None:
        return 0
    temp =linked_list_traversal2(current.next)
    result=result+current.val+temp

    return result

# def linked_list_traversal2(head):
#     if head is None: return 0
#     return head.val+linked_list_traversal(head.next)


print(linked_list_traversal2(a))