
def fibonacciIterative(n):
    fib_res_i = 1
    fib_res_i1 = 0

    for i in range(1, n):
        tmp = fib_res_i
        fib_res_i = fib_res_i + fib_res_i1
        fib_res_i1 = tmp
        
    return fib_res_i


def fibonacciRecursive(n):
    """
    a(n+1) = a(n) + a(n-1)
    """
    if n == 1: return 1
    if n == 0: return 0

    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    


print(fibonacciIterative(3))
print(fibonacciRecursive(12))