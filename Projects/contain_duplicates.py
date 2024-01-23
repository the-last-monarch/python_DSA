# Question:
# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example:
#     Input: nums = [1,2,3,1]
#     Output: true

# Solution:
def contain_duplicates(list):
    seen = set()
    for num in list:
        if num in seen:
            return True
        seen.add(num)
    return False

myList = [1,2,3,1]
print(contain_duplicates(myList))