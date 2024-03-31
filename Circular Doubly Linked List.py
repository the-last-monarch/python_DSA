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
    
    def __str__(self) -> str:
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head: break
            result += ' <-> '
        return result
        
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
    
    def prepend(self, value):
        new_node = Node(value) #------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.length == 0: #--------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node
            self.tail = new_node #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = new_node
            new_node.prev = new_node
        else: #------------------------------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.tail.next = new_node
            self.head.prev = new_node #------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1 #------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def traverse(self):
        current_node = self.head #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        while current_node: #---------------------------------------------- Time Complixity = O(n) because of "while loop" Space Complixity = O(1)
            print(current_node.value) #------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            current_node = current_node.next
            if current_node == self.head: #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
                break
    
    def reverse_traverse(self):
        current_node = self.tail #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        while current_node: #---------------------------------------------- Time Complixity = O(n) because of "while loop" Space Complixity = O(1)
            print(current_node.value)
            current_node = current_node.prev #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
            if current_node == self.tail: #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
                break
            
        
new_cdll = CircularDoublyLinkedList()

new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.append(40)
new_cdll.prepend(90)
print(new_cdll)
new_cdll.traverse()
new_cdll.reverse_traverse()