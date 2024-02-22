# # What is Tuples?
# # A tuple is immutable sequence of python objects. Tuples are also comparable and hashable.

# newTuple = ('a', 'b', 'c', 'd', 'e')
# againTuple = ('a', ) # Tuple with single element
# anotherTuple = tuple() # Empty tuple
# onceAgainTuple = tuple('batman') # Now tuple function divide every alphabet in an element here

# print(newTuple)
# print(againTuple)
# print(anotherTuple)
# print(onceAgainTuple)

# # # Time Complexity = O(1)
# # # Space Complexity = O(n)


# # How to access Tuples
# newTuple = ('a', 'b', 'c', 'd', 'e')

# print(newTuple[1])
# print(newTuple[-3])

# # Syntex = tuple[leftIndex:rightIndex] Right Index wouldn't include here
# print(newTuple[1:3])
# print(newTuple[:3])
# print(newTuple[2:])
# print(newTuple[:])


# # Traversing a Tuple

# newTuple = ('a', 'b', 'c', 'd', 'e')

# for i in newTuple:
#     print(i)

# for i in range(len(newTuple)):
#     print(newTuple[i])

# # Time Complexity :- O(n)
# # Space Complexity :- O(1)


# # Searching for an element in Tuple

newTuple = ('a', 'b', 'c', 'd', 'e')

# print('a' in newTuple) # -------------> Time Complexity = O(n)

# print(newTuple.index('f')) # -------------> Time Complexity = O(n)

def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)): # -----------------------------> Time Complexity = O(n)
        if p_tuple[i] == element: # --------------------------------> Time Complexity = O(1)
            return f"The {element} in found on {i} index" # --------> Time Complexity = O(1)
    return "The element is not present in tuple" # -----------------> Time Complexity = O(1)
# # Time complexity = O(n)
# # Space complexity = O(1)
print(searchTuple(newTuple, 'z'))