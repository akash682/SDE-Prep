"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

https://leetcode.com/problems/valid-parentheses/
"""
"""
## Inputs
s = "" --> True
s = "("
s = "([{}])" --> Valid
s = "([)]{" --> Not Valid
s = "([{}]){" 

# Pseudo Code
# Psuedo Code 書く（Data Structure Stack LIFO、Close Bracket Close ）
# How to optimize? (Code の Optimize, logN)
# Don't use this/that/it
# The conversation is one way, TestCase は聞いて良い
# TestCase WalkThrough する必要ある？Edge ケースだけで良い？
# 何に詰まっているか、どの DataStructure/Algorightm を使うか分からない。
# Readability
# Tries/BFS/DFS
"""

## Brute Force Approach
open_seen = []

def isvalidbracket(s):
    hash_bracket = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open_seen = []
    for i in range(len(s)):
        if s[i] not in hash_bracket:
            open_seen.append(s[i])
        elif s[i] in hash_bracket:
            if open_seen.pop() != hash_bracket[s[i]]:
                return False
    if not open_seen:
        return True
    else:
        return False

isvalidbracket("(((")  # 1, works 
#open_seen = [(,(,(]

isvalidbracket("((()))") #2, ???? 

# TestCase 1
s = "([{}])"
open_seen =['(', '[', '{']
open_seen = ['(', '[']
open_seen = []

# TestCase 2
s = "([)]{"
open_seen = ['(', '[']

# TestCase 3
s = "([{}]){"
open_seen = []
open_seen = ['{']

# TestCase 4