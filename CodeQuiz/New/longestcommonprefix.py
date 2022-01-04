"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    """
    #Brute Force Approach
    def findlongeststring(self,strs):
    min_length = 201
    for i in range(len(strs)):
        if len(strs[i]) < min_length:
            min_length = len(strs[i])
    return min_length

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        
        min_length = self.findlongeststring(strs)
        res_str = ""
        for i in range(min_length):
            com_char = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != com_char:
                    return res_str
            res_str += com_char
        return res_str
    """
    def longestCommonPrefix(self, strs):
        res = []
        
        size = min([len(i) for i in strs])
        for idx in range(size):
            chars = set([w[idx] for w in strs])
            if len(chars) == 1:
                res.append(strs[0][idx])
            else:
                break
        
        return "".join(res)

strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))