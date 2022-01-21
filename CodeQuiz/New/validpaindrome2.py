"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.

"""
from ctypes import pointer


def validPalindrome(s):
    if s == " ":
        return True

    if s == s[::-1]:
        return True
    else:
        s_back = s[::-1]
        for pointer in range(len(s)):
            if s[pointer] != s_back[pointer]:
                option1 = s[:pointer] + s[pointer+1:]
                option2 = s_back[:pointer] + s_back[pointer+1:]
                if option1 == option1[::-1] or option2 == option2[::-1]:
                    return True
                else:
                    return False
        return True

s = "aba"
print(validPalindrome(s))

s = "abca"
print(validPalindrome(s))

s = "abc"
print(validPalindrome(s))

s = "deeee"
print(validPalindrome(s))