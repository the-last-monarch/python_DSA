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
    
    def __str__(self):
            temp_node = self.head
            result = ""
            while temp_node is not None:
                result += str(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
                result += '->'
            return result
    
    def append(self, value):
        new_node = Node(value) #---------------------------- Time Complixity = O(1) Space Complixity = O(1) because we are adding only 1 element in the end 
        if self.length == 0: #------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node #-------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.tail = new_node
            new_node.next = new_node #---------------------- Time Complixity = O(1) Space Complixity = O(1)
        else:
            self.tail.next = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = self.head
            self.tail = new_node
        self.length += 1 #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def prepend(self,value):
        new_node = Node(value) #---------------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.head is None: #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node
            self.tail = new_node #-------------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node #-------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.tail.next = new_node
        self.length += 1 #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0: #-------------- Time Complixity = O(1) Space Complixity = O(1)
            raise Exception("Index is out of range")
        if index == 0: #------------------------------------ Time Complixity = O(1) Space Complixity = O(1)
            if self.length == 0: #-------------------------- Time Complixity = O(1) Space Complixity = O(1)
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node #------------------ Time Complixity = O(1) Space Complixity = O(1)
            else: #----------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length: #------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:  #-------------------------------------------- Time Complixity = O(1) Space Complixity = O(1)
            temp_node = self.head
            for _ in range(index - 1): #-------------------- Time Complixity = O(n) because of "for loop" Space Complixity = O(1)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
        self.length += 1 #---------------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def traverse(self):
        current = self.head #------------------------------- Time Complixity = O(1) Space Complixity = O(1)
        while current is not None: #------------------------ Time Complixity = O(n) because of "while loop" Space Complixity = O(1)
            print(current.value)
            current = current.next
            if current == self.head: #---------------------- Time Complixity = O(1) Space Complixity = O(1)
                break
        
cslinkedlist = CSLinkedList()
# print(cslinkedlist.head)
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.insert(0, 50)
print(cslinkedlist)
cslinkedlist.insert(5, 60)
print(cslinkedlist)
cslinkedlist.traverse()
# print(cslinkedlist.tail.value)
# print(cslinkedlist.head.value)
# print(cslinkedlist.head.next.value)