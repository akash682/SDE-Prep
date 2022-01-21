class Solution:
    def plusOne(self, digits):
        tmp_num = 0
        for i in range(len(digits)):
            tmp_num += 10**(len(digits)-i-1)*digits[i]
        
        tmp_num += tmp_num + 1
        return tmp_num.split('')

mySolution = Solution()
mySolution.plusOne([1,2,4])