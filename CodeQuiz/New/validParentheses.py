"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input1: s = "()"
Input2: s = "()[]{}"
Input3: s = "(]"
"""

def isValid(s):
    hash_close = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    track_openbracket = []
    track_latest_openbracket = ""
    if len(s) == 1:
        return False
    for i in range(len(s)):
        # Found a closing bracket
        if s[i] in hash_close:
            if hash_close[s[i]] != track_latest_openbracket:
                return False
            else:
                track_latest_openbracket = track_openbracket.pop()
        # Found a opening bracket
        else:
            track_openbracket.append(track_latest_openbracket)
            track_latest_openbracket = s[i]
    # IF there is something left in the openbracket stack
    if track_openbracket:
        return False

    return True

s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))