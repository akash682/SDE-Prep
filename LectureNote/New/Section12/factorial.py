from gettext import find


def findFactorialRecursive(number):
    if number == 1:
        return number
    else:
        return number*findFactorialRecursive(number-1)


print(findFactorialRecursive(4))

def findFactorialIterative(number):
    ans = 1
    for i in range(1, number+1):
        ans *= i
    return ans

print(findFactorialIterative(4))