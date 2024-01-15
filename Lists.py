# # Creating different Lists

# intergerList = [1,2,3,4]
# print(intergerList)

# stringList = ["shadow", "dark", "bright"]
# print(stringList)

# mixList = [1, "a", 1.2]
# print(mixList)

# nestedList = ["abc", 1, 2, [1.3, 4], ["str", "int"]]
# print(nestedList)


# # Accessing/Traversing a List

# shoppingList = ["milk", "ghee", "cheese", "amulButter", "vegtables", "fruits"]

# print(shoppingList[0])
# print("Butter" in shoppingList) # If this return 'True' means the element is present in list
# print(shoppingList[-4])
# for i in shoppingList:
#     print(i)
# for i in range (len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"
#     print(shoppingList[i])

# emptyList = []
# for i in emptyList:
#     print("This will never print. Because list is empty.")


# # Update/ Insert in a List

# myList = [1,2,3,4,5,6]
# print(myList)

# myList[2] = 22
# myList[3] = 33
# print(myList)

# myList.insert(0,11) --------------------------→ Time Complixity = O(n) Space Complixity = O(1)
# print(myList)
# myList.append(10) ----------------------------→ Time Complixity = O(1) Space Complixity = O(1)
# print(myList)
# newList = [100, 99, 98, 97]
# myList.extend(newList) --------------------------→ Time Complixity = O(n) Space Complixity = O(n)
# print(myList)


# # Slicing/Deleting a List

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# print(myList[0:2])
# myList[0:2] = ['x', 'y']
# print(myList[:])

# print(myList.pop(2)) --------------------------→ Time Complixity = O(1)/O(n) Space Complixity = O(1)
# print(myList)
# del myList[2:4] --------------------------→ Time Complixity = O(n) Space Complixity = O(1)
# print(myList)
# myList.remove('f') --------------------------→ Time Complixity = O(n) Space Complixity = O(1)
# print(myList)


# # Serching for an element in the List
# my_list = [10,20,30,40,50,60,70,80,90]
# in operator
# target = 60
# if target in my_list:
#     print(f"{target} is present in the my_list")
# else:
#     print(f"{target} is not present in the my_list")

# Liner Search
# def linerSearch(list, target):
#     for i,value in enumerate(list): # --------------------------→ Time Complixity = O(n) Space Complixity = O(1)
#         if value == target:
#             return i
#     return -1

# print(linerSearch(my_list, target))