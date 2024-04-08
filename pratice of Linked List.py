# # Pratice of Linked List

# Ouestion 1 :- 
# Return the Nth term

# Solution 1 :-
from LinkedList import LinkedList

def nthTerm(ll, n):
    pointer1 = ll.head #--------------------------------- Time Complixity = O(1)  Space Complixity = O(1)
    pointer2 = ll.head
    
    for i in range(n): #--------------------------------- Time Complixity = O(n)  Space Complixity = O(1)
        if pointer2 is None: #--------------------------- Time Complixity = O(1)  Space Complixity = O(1)
            return None
        pointer2 = pointer2.next
    
    while pointer2: #----------------------------------- Time Complixity = O(n)  Space Complixity = O(1)
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1 #----------------------------------- Time Complixity = O(1)  Space Complixity = O(1)

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthTerm(customLL, 4))