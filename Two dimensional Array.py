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
