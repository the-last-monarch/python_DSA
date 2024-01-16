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


# # List Operations/Functions
# a = [1,2,3]
# b = [4,5,6]
# c = a + b   # Here, '+' is an operator
# print(c)

# d = [0]
# d = d * 4
# print(d)

# e = [1,2,3,4,5,6,7]
# print(len(e))
# print(max(e))
# print(min(e))
# print(sum(e))
# # Avergae
# print(sum(e)/len(e))

# mylist = list()
# while True:
#     inp = input("Enter the numbers you want average:")
#     if inp == 'done': break
#     value = float(inp)
#     mylist.append(value)
# average = sum(mylist)/len(mylist)
# print("Avergae:",average)


# # String to a List
# a = 'spam'
# b = list(a)
# print(b)

# c = 'spam-spam1-spam2'
# x = '-'
# d = c.split(x)
# print(d)
# print(x.join(d))


# # Pitfalls and avoid of list
# myList = [4,3,6,1,9,0]
# orig = myList[:]
# myList = myList.sort()
# print(myList)

# myList.append([10])
# print(myList)

# myList.sort()
# print(myList)

# print(sorted(myList))
# print(orig)


# # Array vs Lists
# import numpy as np
# myArray = np.array([1,2,3,4,5,6, 'a']) # Here int also convert in str
# myList = [1,2,3,4,5,6] # Here int stay int and str stay as str

# print(myArray/2)
# print(myArray)
# print(myList/2)
# print(myList)


# # Time and Space complixity of List
# # Creating an empty list ---------------→ Time Complixity = O(1)        Space Complixity = O(1)
# # Creating a List with element ---------------→ Time Complixity = O(n)        Space Complixity = O(n)
# # Inserting a value in List ---------------→ Time Complixity = O(n)        Space Complixity = O(1)
# # Traversing a List ---------------→ Time Complixity = O(n)        Space Complixity = O(1)
# # Accessing a given List ---------------→ Time Complixity = O(1)        Space Complixity = O(1)
# # Searching a given value in List ---------------→ Time Complixity = O(1)        Space Complixity = O(1)
# # Deleting a value from List ---------------→ Time Complixity = O(n)        Space Complixity = O(1)


# # List Comprehension
# prev_list = [1,2,3,4]
# new_list = []
# for i in prev_list:
#     multiply_2 = i * 2
#     new_list.append(multiply_2)

# # new_list = [new_list for item in list]

# new_list = [i * 2 for i in prev_list]
# print(prev_list)
# print(new_list)

# language = "python"
# new_list2 = [letter for letter in language]
# print(new_list2)


# # Conditional List Comprehension
# # new_list = [new_item for item in list if condition]

# oldList = [12,-9,34,6,-1,5,-90]
# newList = [number for number in oldList if number > 0]
# print(newList)

# newList = [number * number for number in oldList if number < 0]
# print(newList)

# sentence = "I am Laptop"

# def is_constant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels
# print(is_constant("z"))
# constants = [i for i in sentence if is_constant(i)]
# print(constants)

# def get_number(number):
#     if number > 0:
#         return number
#     else:
#         return "negative number"
    # return number if number > 0 else "negative number"
    
# new_List = [number if number > 0 else 0 for number in oldList]
# print(new_List)

# new_List = [get_number(number) for number in oldList]
# print(new_List)