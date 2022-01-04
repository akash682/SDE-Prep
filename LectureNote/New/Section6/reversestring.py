"""
Create a function that reverses a string:
'Hi My Name is Andrei should be:
'ierdnA si eman vM iH
"""

def reverseString(str):
    result = ""
    if str == "":
        return ""

    for i in range(len(str)):
        result += str[len(str) - 1 - i]
    
    return result

def reverseString2(str):
    return str[::-1]

input = "Hi My Name is Andrei"
print(reverseString(input))
print(reverseString2(input))