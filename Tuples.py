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
# newTuple = ('a', 'b', 'c', 'd', 'e')

# print('a' in newTuple) # -------------> Time Complexity = O(n)

# print(newTuple.index('f')) # -------------> Time Complexity = O(n)

# def searchTuple(p_tuple, element):
#     for i in range(0, len(p_tuple)): # -----------------------------> Time Complexity = O(n)
#         if p_tuple[i] == element: # --------------------------------> Time Complexity = O(1)
#             return f"The {element} in found on {i} index" # --------> Time Complexity = O(1)
#     return "The element is not present in tuple" # -----------------> Time Complexity = O(1)
# # Time complexity = O(n)
# # Space complexity = O(1)
# print(searchTuple(newTuple, 'z'))


# # Tuple Function / Operations
# tuple1 = (1,2,3,4,5)
# tuple2 = (10,9,8,7,6)

# print(tuple1 + tuple2)
# print(tuple1 * 4)
# print(4 in tuple1)
# print(tuple1.count(2))
# print(tuple1.index(4))
# print(len(tuple2))
# print(max(tuple2))
# print(min(tuple1))
# print(tuple([1,2,3,4]))


# # Tuple vs Lists

# # List is mutable, whereas a Tuple is immutable.

# list1 = [0,1,2,3,4,5,6]
# tuple1 = (0,1,2,3,4,5,6)
# list1[3] = 10
# list1 = [6,5,4,3,2,1,0]
# del list1[0]
# print(list1)

# tuple1[3] = 10
# tuple1 = (6,5,4,3,2,1,0)
# del tuple1[4]
# print(tuple1)

# # Functions that can be used for both List and Tuples. len(), max(), min(), sum(), any(), all() and sorted().
# # Tuples can be stored in Lists. And Lists can be stored in Tuples.
# list2 = [(1,2), (3,4), (5,6)]
# tuple2 = ([1,2], [3,4], [5,6])
# print(list2)
# print(tuple2)
init_tuple_a = 1, 2
init_tuple_b = (3, 4)   
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]