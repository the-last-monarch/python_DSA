class Node:
    def __init__(self, value):
        self.value = value #----------------------------------------------- Time Complixity = O(n) because we are creating new Node Space Complixity = O(1)
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def append(self, value):
        new_node = Node(value) #------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node #------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1 #------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        
new_cdll = CircularDoublyLinkedList()

new_cdll.append(10)
new_cdll.append(20)
print(new_cdll.tail)