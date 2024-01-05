# 1. Big O - O(1)
    # # In this method number of operation will always be one. No matter what is value of n.

# #def multiply_numbers(n):
# #    return n*n

# # print(multiply_numbers(5))


# 2. Big O - O(n)
    # # Program will run "n" times when ever you run it.

# #def Numbers(n):
#     # for i in range(n):
#         # print(i)
# # Numbers(10)


# 3. Drop Constant
    # # In below program we will see why we drop constant in Big O - O(n) Algrothim.

# #def Numbers(n):
# #     for i in range(n):
# #         print(i)
# #     for j in range(n):
# #         print(j)
# # Numbers(10)

    # # Whenever you calculate the Big O complexity of any algorithm, you can throw out or ignore the constants. This is O(2n), which simplifies to just O(n).
    # # This is O(1 + n/2 + 100), which simplifies to just O(n).
    # # Constant have no big deal with program.


# 4.Big O - O(n^2)
    # # This type of code is inenfficent code
# #def numbers(n):
# #     for i in range(n):
# #         for j in range(n):
# #             print((i,j))
            
# # numbers(10)
    # # The above code run 100 times to get the output


# 5. Non Dominant Terms
    # #Big O(n^2 + n) This is actual represention of this method but we will write it as Big O(n^2)
    # #because "n^2" is more dominant than "n" so we can ignore "n" and it won't affect number of operations.
    
# # def numbers(n):
# #     for i in range(n):
# #         for j in range(n):
# #             print((i,j))
            
# #     for k in range(n):
# #         print(k)

# #numbers(10)


# 6. Big O - O(logN)

# O(log N) is a common runtime complexity.
# Examples include binary searches, finding the smallest or largest value in a binary search tree, and certain divide and conquer algorithms.
# If an algorithm is dividing the elements being considered by 2 each iteration, then it likely has a runtime complexity of O(log N)


# Space compxlexity
# def sum(n):
#     if n <= 0:
#         return 0
#     return n + sum(n-1)

# print(sum(3))

# def pair_sum_sequence(n):
#     total = 0
#     for i in range(n):
#         total = total + pair_sum(i, i+1)
#     return total

# def pair_sum(a, b):
#     return a + b

# pair_sum_sequence(4)


# # Different Terms for Input - Add vs Multiply
# # A) If your algorithm is in the form "do this, then when you are all done , do that" then you ADD the runtimes.
                                # # ADD THE RUNTIMES :- O(A + B)
                                
def print_items(a, b):
    for i in range (a):
        print(i)
        
    for j in range (b):
        print(j)

# # B) If your algorithm is in the form "do this for each time you do that" then you MULTIPLY the runtimes.
                                # # MULTIPLY THE RUNTIMES :- O(A*B)
                                
def print_items(a, b):
    for i in range (a):
        for j in range (b):
            print(a, b)
