def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i,j)
my_list = [1,2,3,4,5,6,7,8,9]
two_sum(my_list, 5)