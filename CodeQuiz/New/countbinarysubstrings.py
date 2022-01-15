"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Constraints:

    1 <= s.length <= 105
    s[i] is either '0' or '1'.

"""


from ctypes import resize


def countBinarySubstrings(s):
    result = 0
    for i in range(2, len(s)+1, 2):
        for j in range(len(s)-i+1):
            it = int(i/2)
            pattern = ['0'*it + '1'*it, '1'*it + '0'*it]
            hikaku = s[j:j+i]
            if hikaku in pattern:
                result += 1
    return result

s = '01'
print(countBinarySubstrings(s))

def countBinarySubstrings(s):
    result = 0
    for i in range(len(s)):
        hikaku = s[i:i+2]
        if hikaku in ['01', '10']:
            result += 1
            j = 1
            while True:
                if i-j >=0 and i+2+j <len(s):
                    if hikaku[0] == s[i-j] and hikaku[1] == s[i+1+j]:
                        result +=1
                        j += 1
                else:
                    break

    return result

s = '01'
print(countBinarySubstrings(s))
