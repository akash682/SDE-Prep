class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res_word = ""
        flag = False
        pointer = len(s) -1
        while True:
            if flag == True and s[pointer] == " ":
                break
            elif pointer < 0:
                return len(res_word)
            else:
                if s[pointer] != " ":
                    res_word += s[pointer]
                    flag = True
                pointer -= 1
        
        return len(res_word)