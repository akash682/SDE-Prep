def isPalindrome(s):
    s = s.lower()
    result = ""
    for i in range(len(s)):
        if s[i].isalnum():
            result += s[i]
        
    if result == result[::-1]:
        return True
    else:
        return False