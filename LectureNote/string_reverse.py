#Implement a function that reverses a string using iteration...and then recursion!


def reverseString_itr(word):
    res = ""
    for i in range(len(word)):
        res += word[- 1 - i]
    return res

def reverseString_rec(word):
    # reverseString_rec = word[0] + reverseString(word[1:])
    if len(word) == 1:
        return word
    return reverseString_rec(word[1:]) + word[0]

itr1 = reverseString_itr('yoyo mastery')
rec1 = reverseString_rec('yoyo_mastery')

print(itr1,rec1)