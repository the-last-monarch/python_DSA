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

# new_node = Node(10)
# print(new_node)

newDDL = DoublyLinkedList()
newDDL.append(10)
newDDL.append(20)
newDDL.append(30)
print(newDDL)
newDDL.prepend(40)
print(newDDL)
# newDDL.traverse()
# newDDL.ReverseTraverse()
print(newDDL.search(10))