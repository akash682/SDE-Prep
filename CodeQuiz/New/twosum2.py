class Solution:
    def twoSum_hash(self, numbers, target):
        hash_map = {}
        for i in range(len(numbers)):
            if numbers[i] not in hash_map:
                hash_map[target - numbers[i]] = i
            else:
                return [hash_map[numbers[i]]+1, i+1]
        
        return -1

    def twoSum_pointer(self,numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        
        return -1

    def __init__(self) -> None:
        pass
