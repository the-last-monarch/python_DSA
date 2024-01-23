# Question:
# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.
# Example:
#     remove_duplicates([1, 1, 2, 2, 3, 4, 5])
#     Output : [1, 2, 3, 4, 5]

# Solution:
def remove_duplicates(list):
    unique_list = []
    seen = set()
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
            seen.add(item)
    return unique_list

my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]