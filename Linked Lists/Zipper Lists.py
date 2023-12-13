class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

#linked List 1
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e= Node("E")


a.next=b
b.next=c
c.next=d
d.next = e

#linked List 2
x = Node('X')
y = Node('Y')
z = Node('Z')

x.next=y
y.next=z

#iterative
def zipper_lists(head1,head2):
    tail = head1
    current1= head1.next
    current2 = head2
    count=0

    while(current1 is not None and current2 is not None):
        if(count %2 ==0):
            tail.next = current2
            current2 = current2.next 
        else:
            tail.next = current1
            current1 = current1.next

        tail= tail.next
        count+=1

    if current1 is None:
        tail.next = current2 

    if current2 is None:
        tail.next = current1


    return traversal(head1)


def traversal(head):
    if head is None: return 
    print(head.val)
    traversal(head.next)



print(zipper_lists(a,x))