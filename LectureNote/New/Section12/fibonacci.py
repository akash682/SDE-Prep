def fibonavviIterative(n):
    prev_2 = 0
    prev_1 = 1
    ans = 0
    if n < 2:
        return n

    for i in range(n-1):
        ans = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = ans
    return ans

print(fibonavviIterative(0))
print(fibonavviIterative(1))
print(fibonavviIterative(2))
print(fibonavviIterative(3))
print(fibonavviIterative(4))
print(fibonavviIterative(5))
print(fibonavviIterative(6))

def fibonavvirecursive(n):
    if n < 2:
        return n
    else:
        return fibonavvirecursive(n-1) + fibonavvirecursive(n-2)

print(fibonavvirecursive(0))
print(fibonavvirecursive(1))
print(fibonavvirecursive(2))
print(fibonavvirecursive(3))
print(fibonavvirecursive(4))
print(fibonavvirecursive(5))
print(fibonavvirecursive(6))
