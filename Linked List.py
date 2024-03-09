# # Linked List is a form of a sequential collection and it does not have to be in order. A Linked List is made up of independent nodes that may contains any type of data
# # and each node has a reference to the next node in the link.

# # Type of Linked Lists:-
# # 1. Singly Linked List
# # 2. Circular Linked List
# # 3. Doubly Linked List
# # 4. Circular Doubly Linked List


# # Node Class Constructor
class Node:   # Time Complixity = O(1), Space Complixity = O(1)
    def __init__(self, value):
        self.value = value
        self.next = None

# new_node = Node(10)
# print(new_node)

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(10)   # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.head = new_node  # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.tail = new_node  # ------------->  Time Complixity = O(1), Space Complixity = O(1)
#         self.length = 1   # ----------------->  Time Complixity = O(1), Space Complixity = O(1)

# # Empty Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)   # -------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.head is None:   # --------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.head = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
            self.tail = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
        else:
            self.tail.next = new_node   # ------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.tail = new_node   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
        self.length += 1
        
    def prepend(self, value) :
        new_node = Node(value)   # ------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.head is None:   # -------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.head =  new_node   # ---------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.tail =  new_node   # ---------------------->  Time Complixity = O(1), Space Complixity = O(1)
        else:
            new_node.next = self.head   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
            self.head = new_node   # ----------------------->  Time Complixity = O(1), Space Complixity = O(1)
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)   # --------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        temp_node = self.head   # ---------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if index < 0 or self.length > 0:   # ----------------------->  Time Complixity = O(1), Space Complixity = O(1)
            return False   # --------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        elif self.length == 0:   # --------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.head = new_node
            self.tail = new_node
        elif index == 0:   # --------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            new_node.next = self.head
            self.head = new_node
        else:       # ---------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            for _ in range(index-1):   # --------------------------->  Time Complixity = O(n), Space Complixity = O(1)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node   # -------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        self.length += 1
        return True
# # Time Complixity in insert will be O(n), Space Complixity = O(1)

    def traverse(self):
        current = self.head
        while current is not None:   # --------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            print(current.value)
            current = current.next
# # Time Complixity in traverse will be O(n), Space Complixity = O(1)

    def search(self, target):
        current = self.head   # --------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
        index = 0
        while current:   # -------------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            if current.value == target:   # --------------------------->  Time Complixity = O(n), Space Complixity = O(1)
                return index
            current = current.next   # -------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            index += 1
        return -1
# # Time Complixity in traverse will be O(n), Space Complixity = O(1)
















new_linked_list = LinkedList()
new_linked_list.insert(1,50)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
# print(new_linked_list)
# # print(new_linked_list.length)
new_linked_list.prepend(40)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(30))