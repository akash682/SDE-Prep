class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
          
        pointer = 0
        res = []
        for i in range(numRows):
            res.append([])
        
        while pointer < len(s):
            idx = (pointer)%(2*numRows-2)
            if idx < numRows:
                res[idx].append(s[pointer])
                pointer += 1
            else:
                tmp = numRows - idx%numRows - 2
                res[tmp].append(s[pointer])
                pointer += 1
                
        res_str =""
        for i in range(len(res)):
            for j in range(len(res[i])) :
                res_str += res[i][j]
        
        return res_str