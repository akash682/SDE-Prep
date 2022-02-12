class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        rec = [1] * len(nums) # rec[i] records the length of the longest increasing subsequence ending with nums[i]
        maxlen = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    rec[i] = max(rec[i], rec[j] + 1)
            maxlen = max(maxlen, rec[i])
        return maxlen

mySolution = Solution()
nums = [10,9,2,5,3,7,101,18]
print(mySolution.lengthOfLIS(nums))