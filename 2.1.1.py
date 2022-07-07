"""Using Figure 2.2 illustrate the operation of insertion-sort on the array A = [31,41,59,26,41]"""

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]


        while list_a[i-1] > value_to_sort and i >0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1
        

    

    # print(list_a)


insertion_sort(list_a = [31,41,59,26,41])

            
# Two Sum – Medium
# Problem
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

def TwoSum(nums, target):
    indexing_length = range(1, len(nums))
    for i in indexing_length:
        value_to_sort = nums[i]

        while value_to_sort + nums[i-1] != target and i >0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
            print(nums[i])
            print(nums[i-1])
        else:
            if value_to_sort + nums[i-1] == target and i >0:
                return value_to_sort, nums[i-1]
    # print(f'nums=>{nums}, target=>{target}, indexing length=> {indexing_length}')

TwoSum(nums=[2, 7, 11, 15], target= 9)
