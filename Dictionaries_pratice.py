# # Question:
# # Count Word Frequency
# # Define a function to count the frequency of words in a given list of words.
# # Example:
# #     words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# #     count_word_frequency(words) 
# # Output:
# #      {'apple': 3, 'orange': 2, 'banana': 1}


# # Solution:
def count_word_frequency(words):
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count
    
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))