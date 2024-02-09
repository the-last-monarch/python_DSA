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