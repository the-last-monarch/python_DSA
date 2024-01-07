# # What is an Array?
# # 1. Array can store data of specified type. 
# # 2. Element in an array is located in a contiguous. 
# # 3. Each element of an array has a unique index.

# # Type of Array
# # There are two type of array
# # 1. One dimensional Array    2. Multi dimensional Array

# 1. One dimensional Array :- An array with bunch of values having been declared with a single index.
# a[i] → i is between 0 and n

# 2. Two dimensional Array :- An array with bunch of values having been declared with double index.
# a[i][j] → i and j between 0 and n

# 3. Three dimensional Array :- An array with bunch of values having been declared with triple index.
# a[i][j][k] → i, j and k between 0 and n

import array
import numpy as np

arr = array.array('i') # ---------------------> O(1)
print(arr)
arr1 = array.array('i', [1,2,3,4]) # -------------------O(n)
print(arr1)
 
np_array = np.array([], dtype = int) # -----------------------O(1)
print(np_array)
np_array1 = np.array([1,2,3,4]) # ---------------------------O(n)
print(np_array1)


# Inserting to an Array

arr2 = array.array('i', [1,2,3,4])
print(arr2)
arr2.insert(0, 5) # -----------------> Max. Space complexity = O(n) and Time complexity = O(1)
print(arr2)


# Traversal Array

arr3 = array.array('i', [1,2,3,4,5])
def traversalArray(array):
    for i in array: # ------------> Time complexity = O(n)
        print(i)    # ------------> Time complexity = O(1)   
# So, Time complexity will be O(n) and Space Complexity will be O(1) because we don't need extra space in memory
traversalArray(arr3)


# Access array element
arr4 = array.array('i', [1,2,3,4,5,6])

def accessArray(array, index):
    if index >= len(array): #------------------------------------> O(1)
        print("There is no element on this index. \nplease enter valid index!") # --------------> O(1)
    else:
        print(array[index]) # -------------------------O(1)
# Time complexity :- O(1)  Space complexity :- O(1)
accessArray(arr4, 0)


# Searching for an element in array

arr5 = array.array('i', [1,2,3,4,5])

def linear_search(arr, target):
    for i in range(len(array)):  # Time complexity --------------- O(n)
        if array[i] == target:   # Time complexity --------------- O(1)
            return i   # Time complexity --------------- O(1)
    return -1
print(linear_search(arr5, 5))

# Time complexity = O(n)
# Space complexity = 0(1)


# Deleting an element in array
# When we delete any element from array it don't just disapper but the next element to it will take it place so there is no empty space will be left.

arr6 = array.array('i', [1,2,3,4,5,6])

arr6.remove(3)
print(arr6)

# if we remove element from the end of array 
# Time complexity = O(1)
# if we remove element from any point from the array
# Time Complexity = O(n)
# Space Complexity = O(1)


######## Time and Space complexity in Array
# Creating an empty array
# Time Complexity = O(1)
# Space Complexity = O(1)

# Creating an Array with element
# Time Complexity = O(n)
# Space Complexity = O(n)

# Inserting a value in Array
# Time Complexity = O(n)
# Space Complexity = O(1)

# Traversing a given Array
# Time Complexity = O(n)
# Space Complexity = O(1)

# Accessing a given cell
# Time Complexity = O(1)
# Space Complexity = O(1)

# Serching a given value
# Time Complexity = O(n)
# Space Complexity = O(1)

# Deleting a given value
# Time Complexity = O(n)
# Space Complexity = O(1)


from array import *

# # 1. Create an array nad traverse.
print("Step 1")
my_array = array('i', [1,2,3,4,5])
for i in my_array : 
    print(i)

# 2. Access individual elements through indexes.
print("Step 2")
print(my_array[1])

# 3. Append any value to the array using append() method.
print("Step 3")
my_array.append(6)
print(my_array)

# 4. Insert any value to the array using insert() method.
print("Step 4")
my_array.insert(0,11)
print(my_array)

# 5. Extend python array using extend() method.
print("Step 5")
my_array2 = array('i', [10,11,12,13])
my_array.extend(my_array2)
print(my_array)

# 6. Add items from list into array using fromlist() method.
print("Step 6")
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any element from array using remove() method.
print("Step 7")
my_array.remove(11)
print(my_array)

# 8. Remove last element from array using pop() method.
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch an element through its index using index() method.
print("Step 9")
print(my_array.index(21))

# 10. Reverse a python array using reverse() method.
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method.
print("Step 11")
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method.
print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 13. Convert array to string using tostring() method.
print("Step 13")
strTemp = my_array.tobytes()
print(strTemp)

# 14. Convert array to a python list with same elements using tolist() method.
print("Step 14")
print(my_array.tolist())

# 15. Append a string to char array using fromstring() method.
print("Step 15")
intTemp = array('i')
intTemp.frombytes(strTemp)
print(intTemp)

# 16. Slice elements from an array.
print("Step 16")
print(my_array[0:4])
print(my_array[4:])
print(my_array[:3])