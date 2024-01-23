# Question:
# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
# Example:
#     pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
#     Output : ['2+5', '4+3', '3+4', '-2+9']

# Solution:
def pair_sum(list, target):
    total = []
    for i in range (len(list)):
        for j in range (i+1, (len(list))):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == target:
                total.append(f"{list[i]}+{list[j]}")
    return total

my_list = [1,2,3,4,5,6,7,8,9,-12,-11,-2,-5]
print(pair_sum(my_list, 7))