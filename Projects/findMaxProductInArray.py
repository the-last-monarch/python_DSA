# Question:
# Find the maximum product of two integers in an array where all elements are positive.

# Solution:
import numpy as np

def maxProduct(arr):
    max1, max2 = 0, 0
    
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            i > max1
    return max1 * max2

myArray = np.array([1,2,3,4,5])
print(maxProduct(myArray))