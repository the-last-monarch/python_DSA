###### TWO DIMENSIONAL ARRAY #######
import numpy as np
twoDArray = np.array([[11,23,21,8], [23, 19, 5, 9], [25, 31, 1, 17], [15, 0, 4, 41]])
print(twoDArray)

# # twoDarray1 = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# # print(twoDarray1)

# twoDarray1 = np.append(twoDArray, [[1,2,3,4]], axis=0)
# print(twoDarray1)


# # Accessing an element of Two Dimensional array
# # a[i][j] -→ i is row index and j is column index
# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) or colIndex >= len(array[0]):
#         print("Incorret Index")
#     else:
#         print(array[rowIndex][colIndex])

# accessElements(twoDArray, 2, 3)

# # Time complexity = O(1)
# # Space complexity = O(1)


# # Traversing Two Dimensional array
# def traverseTDArray(array):
#     for i in range (len(array)):
#         for j in range (len(array[0])):
#             print(array[i][j])

# traverseTDArray(twoDArray)
# # Time Complixity → in line 29 its O(mn) because for every row it should check every column also 
#                     # in line 30 its O(n)
#                     # final  Time Complixity will be O(n∧2)
# # Space Complixity → O(1)


# # Searching Two Dimensional Array
# def seachTDArray(array, value):
#     for i in range (len(array)):
#         for j in range (len(array[0])):
#             if array[i][j] == value:
#                 return "The Value is located at index " + str(i) + " " + str(j)
#     return "Value not found"

# print(seachTDArray(twoDArray, 31))

# # Time Complixity → in line 42 its O(mn) because for every row it should check every column also 
#                     # in line 43 its O(n)
# # Space Complixity → O(1)


# # Deletion Two Dimensional Array
# newTDArray = np.delete(twoDArray, 3, axis=1)
# print(newTDArray)

# # Time Complixity → O(mn)
# # Space Complixity → O(mn)


# # Time and Space Complixity in 2D Array
# # Creating an empty Array ----→ Time complixity: O(1)        Space complixity: O(1)
# # Creating an Array with elements ----→ Time complixity: O(mn)        Space complixity: O(mn)
# # Inserting a row/column in an Array ----→ Time complixity: O(mn)        Space complixity: O(mn)
# # Traversing a given Array ----→ Time complixity: O(mn)        Space complixity: O(1)
# # Accessing a give cell ----→ Time complixity: O(1)        Space complixity: O(1)
# # Searching a given value ----→ Time complixity: O(mn)        Space complixity: O(1)
# # Deleting a column/row ----→ Time complixity: O(mn)        Space complixity: O(mn)



# # When to use and avoid Array

# # When to use Array:
# # 1. To store multiple variables of same data type.
# # 2. When we need to Random Access to given array because it will take O(1) Time Complixity.

# # When to avoid an Array:
# # 1. Storing same data type (in some coding languages it is an issue).
# # 2. Reserve specific memory in storage((RAM)).