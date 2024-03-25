class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # 1 element Circular Singly Linked List
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
        self.head = new_node #------------------------- Time Complixity = O(1) Space Complixity = O(1)
        self.tail = new_node #------------------------- Time Complixity = O(1) Space Complixity = O(1)
        self.length = 1 #------------------------------ Time Complixity = O(1) Space Complixity = O(1)
    
    
    # Empty Circular Singly Linked List
    def __init__(self):
            self.head = None #------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.tail = None #------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.length = 0 #-------------------------- Time Complixity = O(1) Space Complixity = O(1)

cslinkedlist = CSLinkedList()
print(cslinkedlist.head)