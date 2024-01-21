# Question:
# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#     myList = [1, 2, 3, 4]
#     middle(myList)  [2,3]

# Solution:
myList = [1,2,3,4,5,6,7,8,9]

def middleFunction(list):
    return list[1:-1]

print(middleFunction(myList))
