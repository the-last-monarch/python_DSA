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
    
    def search(self, target):
        current_node = self.head #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        while current_node: #---------------------------------------------- Time Complixity = O(n) because of "while loop" Space Complixity = O(1)
            if current_node.value == target: #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
                return True
            current_node = current_node.next
            if current_node == self.head: #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
                break
        return False
    
    def get(self, index):
        if index < 0 or index >= self.length: #---------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return None
        current_node = None
        if index < self.length // 2: #------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            current_node = self.head
            for i in range(index): #--------------------------------------- Time Complixity = O(n/2) because we are traversing through only half list Space Complixity = O(1)
                current_node = current_node.next
        else: #------------------------------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            current_node = self.tail
            for i in range(self.length - 1, index, -1): #------------------ Time Complixity = O(n/2) because we are traversing through only half list Space Complixity = O(1)
                current_node = current_node.prev
        return current_node
    # # The overall Time Complixity will be O(n) because we can eliminate constant 
    
    def set_value(self, index, value):
        temp_node = self.get(index) #-------------------------------------- Time Complixity = O(n) because we are using "get method" here Space Complixity = O(1)
        if temp_node: #---------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            temp_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length: #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
            raise Exception("Index is out of range")
        if index == 0:
            self.prepend(value) #------------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            return
        if index == self.length:
            self.append(value) #------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return
        new_node = Node(value)
        temp_node = self.get(index-1) #------------------------------------ Time Complixity = O(n) because we are using "get method" here Space Complixity = O(1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 0: #--------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return None
        if self.length == 1: #--------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = None
            self.tail = None
        else: #------------------------------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.head = self.head.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1 #-------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
            
            
        
new_cdll = CircularDoublyLinkedList()

new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.append(40)
new_cdll.prepend(90)
print(new_cdll)
# new_cdll.traverse()
# new_cdll.reverse_traverse()
# print(new_cdll.search(80))
# print(new_cdll.get(-1))
# print(new_cdll.set_value(1, 100))
# new_cdll.insert(2, 50)
# new_cdll.pop_first()
new_cdll.pop()
print(new_cdll)