# Given 2D list calculate the sum of diagonal elements.

# Example

#     myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
     
#     diagonal_sum(myList2D) 15

myList = [[1,2,3], [4,5,6],[7,8,9]]

def diagonal_sum(list):
    total = 0
    for i in range(len(list)):
        total += list[i][i]
    return total
print(diagonal_sum(myList))