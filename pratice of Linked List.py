# # # Pratice of Linked List

# # Ouestion 1 :- 
# # Return the Nth term

# # Solution 1 :-
from LinkedList import LinkedList

# def nthTerm(ll, n):
#     pointer1 = ll.head #--------------------------------- Time Complixity = O(1)  Space Complixity = O(1)
#     pointer2 = ll.head
    
#     for i in range(n): #--------------------------------- Time Complixity = O(n)  Space Complixity = O(1)
#         if pointer2 is None: #--------------------------- Time Complixity = O(1)  Space Complixity = O(1)
#             return None
#         pointer2 = pointer2.next
    
#     while pointer2: #----------------------------------- Time Complixity = O(n)  Space Complixity = O(1)
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1 #----------------------------------- Time Complixity = O(1)  Space Complixity = O(1)

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(nthTerm(customLL, 4))

# # Question 2 :-
# # Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

# Solution 2 :- 

def partition(ll, x):
    current_node = ll.head #------------------------------ Time Complixity = O(1)  Space Complixity = O(1)
    ll.tail = ll.head
    
    while current_node: #--------------------------------- Time Complixity = O(n) because of "while loop"  Space Complixity = O(1)
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x: #---------------------- Time Complixity = O(1)  Space Complixity = O(1)
            current_node.next = ll.head
            ll.head = current_node
        else: #------------------------------------------- Time Complixity = O(1)  Space Complixity = O(1)
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node
    
    if ll.tail.next is not None: #------------------------ Time Complixity = O(1)  Space Complixity = O(1)
        ll.tail.next = None

custom_ll = LinkedList()
custom_ll.generate(10, 0, 99)
print(custom_ll)
partition(custom_ll, 30)
print(custom_ll)