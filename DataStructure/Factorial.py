
# Simple Ans
def factorial_recursive(number):
    if number > 1:
        return number*factorial(number-1)
    
    return number

def factorial_iterative(number):
    res = 1
    for i in range(2, number+1):
        res *= i
    
    return res

print(factorial_recursive(6))
print(factorial_iterative(6))