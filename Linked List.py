# # Linked List is a form of a sequential collection and it does not have to be in order. A Linked List is made up of independent nodes that may contains any type of data
# # and each node has a reference to the next node in the link.

# # Type of Linked Lists:-
# # 1. Singly Linked List
# # 2. Circular Linked List
# # 3. Doubly Linked List
# # 4. Circular Doubly Linked List


# # Node Class Constructor
class Node:   # Time Complixity = O(1), Space Complixity = O(1)
    def __init__(self, value):
        self.value = value
        self.next = None

# new_node = Node(10)
# print(new_node)

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(10)   # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.head = new_node  # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.tail = new_node  # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.length = 1   # ----------------->  Time Complixity = O(1), Space Complixity = O(1)

# # Empty Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)   # -------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.head is None:   # --------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.head = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
            self.tail = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
        else:
            self.tail.next = new_node   # ------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.tail = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
        self.length += 1

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.head.value)
print(new_linked_list.length)