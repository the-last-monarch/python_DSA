# Question:
# Find a number in array

# Solution:
import numpy as np

myArray = np.array([1,2,3,4,5,8,7,6,10,9,8,13,12,15,14,11,20,16,17,19,18])

def findNumber(array, number):
    for i in range (len(array)):
        if array[i] == number:
            print(i)

findNumber(myArray, 20)
# print(len(myArray))