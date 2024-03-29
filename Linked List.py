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
# # Time Complixity in "append" will be O(n), Space Complixity = O(1)
        
    def prepend(self, value) :
        new_node = Node(value)   # ------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.head is None:   # -------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.head =  new_node   # ---------------------->  Time Complixity = O(1), Space Complixity = O(1)
            self.tail =  new_node   # ---------------------->  Time Complixity = O(1), Space Complixity = O(1)
        else:
            new_node.next = self.head   # ------------------>  Time Complixity = O(1), Space Complixity = O(1)
            self.head = new_node   # ----------------------->  Time Complixity = O(1), Space Complixity = O(1)
        self.length += 1
# # Time Complixity in "prepend" will be O(n), Space Complixity = O(1)
    
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
# # Time Complixity in "insert" will be O(n), Space Complixity = O(1)

    def traverse(self):
        current = self.head
        while current is not None:   # --------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            print(current.value)
            current = current.next
# # Time Complixity in "traverse" will be O(n), Space Complixity = O(1)

    def search(self, target):
        current = self.head   # --------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        index = 0
        while current:   # -------------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            if current.value == target:   # --------------------------->  Time Complixity = O(1), Space Complixity = O(1)
                return index
            current = current.next   # -------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            index += 1
        return -1
# # Time Complixity in "search" will be O(n), Space Complixity = O(1)

    def get(self, index):
        if index == -1:   # --------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            return self.tail
        if index < -1 or index >= self.length:   # ---------------->  Time Complixity = O(1), Space Complixity = O(1)
            return None
        current = self.head
        for _ in range(index):   # -------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
            current = current.next
        return current   # ---------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
# # Time Complixity in "get" will be O(n), Space Complixity = O(1)

    def set_value(self, index , value):
        temp = self.get(index)   # ---------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
        if temp:
            temp.value = value   # ---------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            return True
        return False   # -------------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
# # Time Complixity in "set" will be O(n), Space Complixity = O(1)

    def pop_first(self):
        if self.length == 0:   # ------------------------------------------>  Time Complixity = O(1), Space Complixity = O(1)
            return None
        popped_node = self.head   # --------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.length == 1:   # ------------------------------------------>  Time Complixity = O(1), Space Complixity = O(1)
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next   # -------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            popped_node.next = None
        self.length -= 1   # ---------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        return popped_node
# # Time Complixity in "pop_first" will be O(1), Space Complixity = O(1)

    def pop(self):
        if self.length == 0:   # ---------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            return None
        popped_node = self.tail   # ------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if self.length == 1:
            self.head = self.tail = None   # ---------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        else:
            temp = self.head   # ---------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
            while temp.next is not self.tail:   # ----------------------------->  Time Complixity = O(n), Space Complixity = O(1)
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node   # ----------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
# # Time Complixity in "pop" will be O(n), Space Complixity = O(1)

    def remove(self, index):
        if index >= self.length or index < -1:   # ------------------------------>  Time Complixity = O(1), Space Complixity = O(1)
            return None
        if index == 0:
            return self.pop_first()   # ----------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        if index == self.length - 1 or index == -1:
            return self.pop()   # ----------------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
        prev_node = self.get(index - 1)   # ------------------------------------->  Time Complixity = O(n), Space Complixity = O(1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None   # --------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        self.length -= 1
        return popped_node.value
# # Time Complixity in "remove" will be O(n), Space Complixity = O(1)

    def delete_all(self):
        self.head = None   # --------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
        self.tail = None
        self.length = 0   # ---------------------------------------------->  Time Complixity = O(1), Space Complixity = O(1)
# # Time Complixity in "delete_all" will be O(n), Space Complixity = O(1)


# # # # # # # # # # # # # # # Time and Space Complexity of Singly Linked List # # # # # # # # # # # # # # # # # 

                                            # Time Complixity            # Space complixity
# # Created                                        O(1)                           O(1)
# # Append                                         O(1)                           O(1)
# # Prepend                                        O(1)                           O(1)
# # Insert                                         O(n)                           O(1)
# # Search                                         O(n)                           O(1)
# # Traverse                                       O(n)                           O(1)
# # Get                                            O(n)                           O(1)
# # Set_value                                      O(n)                           O(1)
# # Pop_first                                      O(1)                           O(1)
# # Pop                                            O(n)                           O(1)
# # Remove                                         O(n)                           O(1)
# # Delete_all                                     O(1)                           O(1)


new_linked_list = LinkedList()

new_linked_list.insert(1,50)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
# print(new_linked_list.length)
new_linked_list.prepend(40)
new_linked_list.traverse()
print(new_linked_list.search(30))
print(new_linked_list.get(-1))
print(new_linked_list.set_value(3, 70))
# print(new_linked_list.pop_first())
# print(new_linked_list.pop_first())
# print(new_linked_list.pop())
print(new_linked_list.remove(4))
print(new_linked_list)
print(new_linked_list.delete_all())
print(new_linked_list)





