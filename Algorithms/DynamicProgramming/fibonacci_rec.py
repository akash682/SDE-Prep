
"""
# My Solution
val_store = {}
calculation = 0
def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    if n-2 in val_store.keys():
        fib_n2 = val_store[n-2]
    else:
        fib_n2 = fib(n-2)
        val_store[n-2] = fib_n2
    
    if n-1 in val_store.keys():
        fib_n1 = val_store[n-1]
    else:
        fib_n1 = fib(n-1)
        val_store[n-1] = fib_n1

    return fib_n1 + fib_n2

"""
val_store = {}
def fib(n):
    if n < 2:
        return n
    if n in val_store.keys():
        return val_store[n]
    
    return fib(n-1) + fib(n-2)
print(fib(7))