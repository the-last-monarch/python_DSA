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
    
    def __str__(self) -> str:
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " <-> "
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node(value) #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.head is None:
            self.head = new_node #------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.tail = new_node
        else: #------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = self.head
            self.head.prev = new_node #------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value) #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if not self.head:
            self.head = new_node #------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.tail = new_node
        else:
            self.tail.next = new_node #------------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 #-------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def traverse(self):
        current_node = self.head
        while current_node: #----------------------------------- Time Complixity = O(n) because of the "while loop" Space Complixity = O(1)
            print(current_node.value)
            current_node = current_node.next #------------------ Time Complixity = O(1) Space Complixity = O(1)
    
    def ReverseTraverse(self):
        current_node = self.tail
        while current_node: #----------------------------------- Time Complixity = O(n) because of the "while loop" Space Complixity = O(1)
            print(current_node.value)
            current_node = current_node.prev #------------------ Time Complixity = O(1) Space Complixity = O(1)
    
    def search(self, target):
        current_node = self.head #------------------------------ Time Complixity = O(1) Space Complixity = O(1)
        index = 0
        while current_node: #----------------------------------- Time Complixity = O(n) because of the "while loop" Space Complixity = O(1)
            if current_node.value == target: #------------------ Time Complixity = O(1) Space Complixity = O(1)
                return index
            current_node = current_node.next #------------------ Time Complixity = O(1) Space Complixity = O(1)
            index += 1
        return False #------------------------------------------ Time Complixity = O(1) Space Complixity = O(1)

    def get(self, index):
        if index < 0 or index >= self.length: #----------------- Time Complixity = O(1) Space Complixity = O(1)
            return None
        if index < self.length // 2: #-------------------------- Time Complixity = O(1) Space Complixity = O(1)
            current_node = self.head
            for _ in range(index): #---------------------------- Time Complixity = O(n/2) because we are traversing through only half list Space Complixity = O(1)
                current_node = current_node.next
        else: #------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            current_node = self.tail
            for _ in range(self.length-1, index, -1): #--------- Time Complixity = O(n/2) because we are traversing through only half list Space Complixity = O(1)
                current_node = current_node.prev
        return current_node #----------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    # # The overall Time Complixity will be O(n) because we can eliminate constant 
    
    def set_value(self, index, value):
        node = self.get(index) #-------------------------------- Time Complixity = O(n) because we are using "get method" here. Space Complixity = O(1)
        if node is not None: #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            node.value = value
            return True #--------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        return False
    
    def insert(self, index, value):
        if index > self.length or index < 0: #------------------ Time Complixity = O(1) Space Complixity = O(1)
            return False
        new_node = Node(value) #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if index == 0:
            self.prepend(value) #------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return
        elif index == self.length:
            self.append(value) #-------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return
        else:
            temp_node = self.get(index-1) #--------------------- Time Complixity = O(n) because we are using "get method" here. Space Complixity = O(1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node #-------------------- Time Complixity = O(1) Space Complixity = O(1)
            temp_node.next = new_node
            self.length += 1
            
    def Popped_first(self):
        if not self.head: #------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return None
        popped_node = self.head #------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.length == 1: #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = None
            self.tail = None
        else: #------------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = self.head.next
            self.head.prev = None #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
            popped_node.next = None
        self.length -= 1 #-------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        return popped_node
    
    def pop(self):
        if self.length == 0: #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            return None
        popped_node = self.tail
        if self.length == 1: #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = None
            self.tail = None #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        else:
            self.tail = self.tail.prev #------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1 #-------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        return popped_node
        

# new_node = Node(10)
# print(new_node)

newDDL = DoublyLinkedList()
newDDL.Popped_first()
newDDL.append(10)
newDDL.append(20)
newDDL.append(30)
# print(newDDL)
newDDL.prepend(50)
newDDL.prepend(60)
print(newDDL)
# newDDL.traverse()
# newDDL.ReverseTraverse()
# print(newDDL.search(10))
# print(newDDL.get(4))
# newDDL.set_value(1,100)
# newDDL.insert(7,100)
# newDDL.Popped_first()
newDDL.pop()
print(newDDL)