# # Dictionaries is a collection of unordered , changeable and index

# my_dict = dict()  # Time Complixity = O(1), Space Complixity = o(1)
# print(my_dict)     

# my_dict2 = {}   # Time Complixity = O(1), Space Complixity = o(1)
# print(my_dict2)

# eng_jap = dict(one='echi', two='ni', three='san')   # Time Complixity = O(n), Space Complixity = o(n)
# print(eng_jap)

# eng_jap2 = {'one':'echi', 'two':'ni', 'three':'san'}    # Time Complixity = O(n), Space Complixity = o(n)
# print(eng_jap2)

# eng_jap_list = [('one','echi'),('two','ni'),('three','san')]    # Time Complixity = O(n), Space Complixity = o(n)
# eng_jap3 = dict(eng_jap_list)    # in "eng_jap_list" we use tuple to make our Dictionary
# print(eng_jap3)


# # # Dictionaries in memory

# # A 'hash table' is a way of doing key-value lookups. You store the values in array, and then use a hash function to find the index of array cell
# # that corresponds to your key-value pairs.


# # Add / Update element in dictionary

# myDict = {'name': 'Shadow', 'age': 30}
# print(myDict)
# myDict['age'] = 19    # Time Complixity = O(1)  Space Complixity = O(n)
# print(myDict)
# myDict['address'] = 'Bharat'    # Time Complixity = O(1)  Space Complixity = amortized O(1)
# print(myDict)


# # Traversing through a Dictionary

# myDict = {'name': 'Shadow', 'age': 30}

# def traverseDict(dict):
#     for key in dict:
#         print(key,':-', dict[key])
# traverseDict(myDict)
# # Time Complixity = O(n)  Space Complixity = O(1)


# # Searching element in Dictionary

# myDict = {'name': 'Shadow', 'age': 30, 'address': 'Bharat'}

# def searchDict(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             return key, value
#     return 'The entered value does not exist'    
# print(searchDict(myDict, 30))
# # Time Complixity = O(n)  Space Complixity = O(1)


# # Deleting an element in Dictionary

# myDict = {'name': 'Shadow', 'age': 19, 'address': 'Bharat', 'study': 'unpad'}
# del myDict['study']   # Time Complixity = O(1)  Space Complixity = O(1)
# print(myDict)

# remove_element = myDict.pop('study', None)    # Now this will not return any error even if the value is not in the Dictionary and even return value of removed/deleted key.
# print(remove_element)   # Time Complixity = O(1)  Space Complixity = O(1)
# print(myDict)

# remove_element_again = myDict.popitem()     # This will remove the last element from the Dictionary
# print(remove_element_again)   # Time Complixity = O(1)  Space Complixity = O(1)
# print(myDict)

# myDict.clear()    # Time Complixity = O(n)  Space Complixity = O(1)
# print(myDict)


# # Dictionary methods

# myDict = {'name': 'Shadow', 'age': 19, 'address': 'Bharat', 'study': 'unpad'}

# myDict_copy = myDict.copy()
# print(myDict_copy)
# print(myDict)

# # newDict = Dictionary.fromkeys(sequence[], values)
# newDict = {}.fromkeys([1,2,3], 0) # if the vlaue is not given it will automatic set value to none
# print(newDict)

# # dictionary.get(key, value) If the key is wrong it will return the entered value.
# print(myDict.get('address', 'india')) # value is optional here but if you enter the wrong value it will return the right value.

# # dictionary.items()
# print(myDict.items())

# # dictionary.keys()
# print(myDict.keys())

# # dictionary.popitem()
# print(myDict.popitem())
# print(myDict)

# # dictionary.setdefult(key, default_value)   # if the dict contain the key but we enter wrong value it will print the value exist in dict.
# print(myDict.setdefault('name', 'shado'))     # And if key doesn't exist then it will create another key with the given value and is value isn't given it will enter None

# # dictionary.pop(key, value)
# print(myDict.pop('name1', 'shakti'))

# # dictionary.values()
# print(myDict.values())

# dictonary.update(other_dictionary)

# newDict = {'x': 'a', 'y': 'b', 'z': 'c'}

# myDict.update(newDict)
# print(myDict)