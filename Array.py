# What is an Array?
# 1. Array can store data of specified type. 
# 2. Element in an array is located in a contiguous. 
# 3. Each element of an array has a unique index.

# Type of Array
# There are two type of array
# 1. One dimensional Array    2. Multi dimensional Array

# # 1. One dimensional Array :- An array with bunch of values having been declared with a single index.
# # a[i] → i is between 0 and n

# # 2. Two dimensional Array :- An array with bunch of values having been declared with double index.
# # a[i][j] → i and j between 0 and n

# # 3. Three dimensional Array :- An array with bunch of values having been declared with triple index.
# # a[i][j][k] → i, j and k between 0 and n

import array

my_array = array.array('i') # ---------------------> O(1)
print(my_array)
my_array1 = array.array('i', [1,2,3,4]) # -------------------O(n)
print(my_array1)

import numpy as np 
np_array = np.array([], dtype = int) # -----------------------O(1)
print(np_array)
np_array1 = np.array([1,2,3,4]) # ---------------------------O(n)
print(np_array1)