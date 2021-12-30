def twoSum(nums, target):
    """
    ## Brute Force Approach
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]  
    """

    ## Hash Table
    hash_sum = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if nums[i] in hash_sum:
            return [hash_sum[nums[i]], i]
        else:
            hash_sum[tmp] = i


#Test
print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
# print(twoSum([])) length is larger than 2, so no need to think about it