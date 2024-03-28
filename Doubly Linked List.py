class Node:
    def __init__(self, value):
        self.value = value #------------------------------------ Time Complixity = O(n) because we are creating new Node Space Complixity = O(1)
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value) #-------------------------------- Time Complixity = O(n) Space Complixity = O(1)
        if not self.head:
            self.head = new_node #------------------------------ Time Complixity = O(n) Space Complixity = O(1)
            self.tail = new_node
        else:
            self.tail.next = new_node #------------------------- Time Complixity = O(n) Space Complixity = O(1)
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 #-------------------------------------- Time Complixity = O(n) Space Complixity = O(1)

# new_node = Node(10)
# print(new_node)

newDDL = DoublyLinkedList()
newDDL.append(10)
newDDL.append(20)
print(newDDL.tail.prev)