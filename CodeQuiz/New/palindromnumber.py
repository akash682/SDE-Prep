# Python Built in 
def isPalindrome(x: int):
    str_x = str(x)
    if str_x[::-1] == str_x:
        return True
    return False

# Check the index contiguously
def isPalindrome(x: int) -> bool:
    str_x = str(x)
    half_len = int(len(str_x)/2)
    for i in range(half_len):
        if str_x[i] != str_x[len(str_x)-1-i]:
            return False
    return True

x = 111
print(isPalindrome(x))