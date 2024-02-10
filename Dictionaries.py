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


# Searching element in Dictionary

myDict = {'name': 'Shadow', 'age': 30, 'address': 'Bharat'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The entered value does not exist'    
print(searchDict(myDict, 30))
# Time Complixity = O(n)  Space Complixity = O(1)


