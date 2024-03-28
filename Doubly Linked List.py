class Node:
    def __init__(self, value):
        self.value = value #------------------------------ Time Complixity = O(n) because we are creating new Node Space Complixity = O(1)
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)


new_node = Node(10)
print(new_node)