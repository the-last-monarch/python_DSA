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
        new_node = Node(value) #----------------------- Time Complixity = O(1) Space Complixity = O(1) because we are adding only 1 element in the end 
        if self.length == 0: #------------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.tail = new_node
            new_node.next = new_node #----------------- Time Complixity = O(1) Space Complixity = O(1)
        else:
            self.tail.next = new_node #---------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = self.head
            self.tail = new_node
        self.length += 1 #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
    
    def prepend(self,value):
        new_node = Node(value) #----------------------- Time Complixity = O(1) Space Complixity = O(1)
        if self.head is None: #------------------------ Time Complixity = O(1) Space Complixity = O(1)
            self.head = new_node
            self.tail = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node #--------------------- Time Complixity = O(1) Space Complixity = O(1)
            self.tail.next = new_node
        self.length += 1 #----------------------------- Time Complixity = O(1) Space Complixity = O(1)
        
cslinkedlist = CSLinkedList()
# print(cslinkedlist.head)
cslinkedlist.append(10)
cslinkedlist.append(20)
print(cslinkedlist)
cslinkedlist.prepend(30)
print(cslinkedlist)
cslinkedlist.prepend(40)
print(cslinkedlist)
# print(cslinkedlist.head.value)
# print(cslinkedlist.head.next.value)
print(cslinkedlist)