"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Input: nums = [1]
Input: nums = [5,4,-1,7,8]
"""
"""
def maxSubArray(nums):
    max_sum = -99999999999
    i = 0
    j = len(nums) - 1
    while i != j:
        subarray = nums[i:j+1]
        max_sum_tmp = sum(nums)
        if max_sum < max_sum_tmp:
            max_sum = max_sum_tmp
        
        if subarray[0] < subarray[-1]:
            i +=1
        else:
            j -=1
    
    return max_sum
"""
#Brute Force Approach
def maxSubArray(nums):
    max_sum = -99999999999
    for i in range(1, len(nums) + 1):
        for j in range(len(nums) - i + 1):
            subArray = nums[j:j+i]
            max_sum_tmp = sum(subArray)
            if max_sum_tmp > max_sum:
                max_sum = max_sum_tmp
    
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
        
nums = [1]
print(maxSubArray(nums))
    
nums = [5,4,-1,7,8]
print(maxSubArray(nums))