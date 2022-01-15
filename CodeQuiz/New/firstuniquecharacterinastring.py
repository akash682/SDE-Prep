"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 
Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""

def firstUniqChar(s):
    has_seen = {}
    for i in range(len(s)):
        if s[i] in has_seen:
            has_seen[s[i]] += 1
        else:
            has_seen[s[i]] = 1
    
    for i in range(len(s)):
        if has_seen[s[i]] == 1:
            return i
    return -1

s = 'loveleetcode'
print(firstUniqChar(s))
