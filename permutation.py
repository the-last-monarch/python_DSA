def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

list1 = ['abc', 'xyz', 'pqr']
list2 = ['xyz', 'pqr', 'abc']
print(permutation(list1,list2))