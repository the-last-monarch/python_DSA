# #  Operations on Stack using List 

# class Stack:
#     def __init__(self):
#         self.list = [] # ---------------------> Time Complixety = O(1), Space Complixety = O(1)
    
#     def __str__(self) -> str:
#         values = [str(x) for x in reversed(self.list)]
#         return '\n'.join(values)


   
#     # isEmpty
#     def isEmpty(self):
#         if self.list == []: # -----------------> Time Complixety = O(1), Space Complixety = O(1)
#             return True
#         else:
#             return False
    
#     # Push
#     def push(self, value):
#         self.list.append(value) # -------------> Time Complixety = O(n) or maybe O(n)^2 if there are too many elements in list, Space Complixety = O(1)
#         return "The element is been added"
#     # pop
#     def pop(self):
#         if self.isEmpty(): # ------------------> Time Complixety = O(1), Space Complixety = O(1)
#             return "The list is already empty"
#         else:
#             return self.list.pop()
        
#     # peek
#     def peek(self):
#         if self.isEmpty(): # ------------------> Time Complixety = O(1), Space Complixety = O(1)
#             return "There is not any element in the stack"
#         else:
#             return self.list[len(self.list) - 1]
    
#     # delete
#     def delete(self): # -----------------------> Time Complixety = O(1), Space Complixety = O(1)
#         self.list = None
    
# customStack = Stack()
# # print(customStack.isEmpty())
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# # print(customStack.pop())
# print(customStack.peek())
# print(customStack)
    


# # Create Stack with limit

# class Stack:
#     def __init__(self, maxSize): # ------------------> Time Complixety = O(1), Space Complixety = O(1)
#         self.maxSize = maxSize
#         self.list = []

#     def __str__(self) -> str: # ---------------------> Time Complixety = O(1), Space Complixety = O(1)
#         values = [str(x) for x in reversed(self.list)]
#         return '\n'.join(values)

#     # isEmpty
#     def isEmpty(self):
#         if self.list == []: # -----------------> Time Complixety = O(1), Space Complixety = O(1)
#             return True
#         else:
#             return False

#     # isFull
#     def isFull(self): # ----------------------> Time Complixety = O(1), Space Complixety = O(1)
#         if len(self.list) == self.maxSize:
#             return True
#         else:
#             return False
    
#     # push
#     def push(self, value):
#         if self.isFull():
#             return "The stack is full"
#         else:
#             self.list.append(value)
#             return "The element is been successfull inserted"
    
#     # pop
#     def pop(self):
#         if self.isEmpty():
#             return "The stack is empty"
#         else:
#             return self.list.pop()
     
#     # peek   
#     def peek(self):
#         if self.isEmpty():
#             return "The stack is empty"
#         else:
#             return self.list[len(self.list) - 1]
    
#     # delete
#     def delete(self):
#         self.list = None

# customStack = Stack(4)
# print(customStack.isEmpty())
# print(customStack.isFull())
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# # print(customStack.isFull())



# Create Stack using Linked List

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


# Operation on Stack using Linked List

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self) -> str: # ---------------------> Time Complixety = O(1), Space Complixety = O(1)
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self): # ----------------------------> Time Complixety = O(1), Space Complixety = O(1)
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value): # ------------------------> Time Complixety = O(1), Space Complixety = O(1)
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self): # --------------------------------> Time Complixety = O(1), Space Complixety = O(1)
        if self.isEmpty():
            return "There is not any element in stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
            
    def peek(self): # -------------------------------> Time Complixety = O(1), Space Complixety = O(1)
        if self.isEmpty():
            return "There is not any element in stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue 
    
    def delete(self): # -----------------------------> Time Complixety = O(1), Space Complixety = O(1)
        self.LinkedList.head = None           
            

customStack = Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
# print("----------")
# customStack.pop()
# print(customStack)
# print(customStack.peek())
print(customStack.delete())
print(customStack)