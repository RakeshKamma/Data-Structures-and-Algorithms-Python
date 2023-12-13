class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')


a.next=b
b.next=c
c.next=d


##A->B->C->D->None

#iterative
def print_list1(head):
   current = head
   while(current is not None):
       print(current.val)
       current=current.next

print(print_list1(a))

#Recursive
def print_list2(head):
    current = head
    if current==None:
        return
    print(current.val)
    print_list2(current.next)


print(print_list2(a))