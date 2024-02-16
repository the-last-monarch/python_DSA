# # Question:
# # Count Word Frequency
# # Define a function to count the frequency of words in a given list of words.
# # Example:
# #     words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# #     count_word_frequency(words) 
# # Output:
# #      {'apple': 3, 'orange': 2, 'banana': 1}


# # Solution:
# def count_word_frequency(words):
#     words_count = {}
#     for word in words:
#         words_count[word] = words_count.get(word, 0) + 1
#     return words_count
    
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# print(count_word_frequency(words))


# # Common Keys
# # Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
# # Example:
# #     dict1 = {'a': 1, 'b': 2, 'c': 3}
# #     dict2 = {'b': 3, 'c': 4, 'd': 5}
# #     merge_dicts(dict1, dict2)

# # Output:
# #     {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# # Solution:
def addDict(dict1, dict2):
    result =  dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(addDict(dict1, dict2))