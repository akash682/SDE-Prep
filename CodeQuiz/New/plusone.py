class Solution:
    def plusOne(self, digits):
        tmp_num = 0
        for i in range(len(digits)):
            tmp_num += digits[i]*10**(len(digits)-i-1)
        
        tmp_num += 1
        return list(str(tmp_num))  

mySolution = Solution()
mySolution.plusOne([1,2,4])