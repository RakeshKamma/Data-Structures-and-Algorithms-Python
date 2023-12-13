class Node:
    def __init__(self,val):
        self.val= val
        self.next_node = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next_node = b
b.next_node = c
c.next_node = d


#Run either one below so that we dont get different answers


#Iterative
def linked_list_traversal1(head):
    current = head
    #assigning new variables
    prev= None
    while(current is not None):
       #for future reference
       next_temp = current.next_node
       #making a connection
       current.next_node=prev
       #updating the variables
       prev= current
       #updating the variables
       current=next_temp

    #printing new head
    return prev.val    

print(linked_list_traversal1(a))  

# #recursive
# def linked_list_traversal2(head,prev=None):
#     current = head
#     #base condition
#     if(current is None): return prev.val
#     next_temp = current.next_node
#     current.next_node = prev
#     return linked_list_traversal2(next_temp,current)



# print(linked_list_traversal2(a))