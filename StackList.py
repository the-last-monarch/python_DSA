class Stack:
    def __init__(self):
        self.list = [] # ---------------------> Time Complixety = O(1), Space Complixety = O(1)
    
    def __str__(self) -> str:
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []: # -----------------> Time Complixety = O(1), Space Complixety = O(1)
            return True
        else:
            return False
    
    # Push
    def push(self, value):
        self.list.append(value) # -------------> Time Complixety = O(n) or maybe O(n)^2 if there are too many elements in list, Space Complixety = O(1)
        return "The element is been added"
    # pop
    def pop(self):
        if self.isEmpty(): # ------------------> Time Complixety = O(1), Space Complixety = O(1)
            return "The list is already empty"
        else:
            return self.list.pop()
        
    # peek
    def peek(self):
        if self.isEmpty(): # ------------------> Time Complixety = O(1), Space Complixety = O(1)
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]
    
    # delete
    def delete(self): # -----------------------> Time Complixety = O(1), Space Complixety = O(1)
        self.list = None
    
    
    
customStack = Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack.pop())
print(customStack.peek())
print(customStack)