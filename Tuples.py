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

newTuple = ('a', 'b', 'c', 'd', 'e')

print(newTuple[1])
print(newTuple[-3])

# Syntex = tuple[leftIndex:rightIndex] Right Index wouldn't include here
print(newTuple[1:3])
print(newTuple[:3])
print(newTuple[2:])
print(newTuple[:])