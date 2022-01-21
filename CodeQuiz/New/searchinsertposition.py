class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
             return 0
        
        N = len(nums)
        mid = int(N/2)
        
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.searchInsert(nums[:mid],target)
        elif target > nums[mid]:
            return mid + self.searchInsert(nums[mid+1:],target) + 1

