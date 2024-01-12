###### TWO DIMENSIONAL ARRAY #######
import numpy as np
twoDarray = np.array([[11,23,21,8], [23, 19, 5, 9], [25, 31, 1, 17], [15, 0, 4, 41]])
print(twoDarray)

# # twoDarray1 = np.insert(twoDarray, 1, [[1,2,3,4]], axis=0)
# # print(twoDarray1)

# twoDarray1 = np.append(twoDarray, [[1,2,3,4]], axis=0)
# print(twoDarray1)


# # Accessing an element of Two Dimensional array
# # a[i][j] -→ i is row index and j is column index
# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) or colIndex >= len(array[0]):
#         print("Incorret Index")
#     else:
#         print(array[rowIndex][colIndex])

# accessElements(twoDarray, 2, 3)

# # Time complexity = O(1)
# # Space complexity = O(1)


