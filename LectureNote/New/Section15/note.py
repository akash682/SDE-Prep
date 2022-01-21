"""
Dynamic Programming: IT is an optimization technque
Do you have something you can cache?
Is a way to solve the problem by breaking down into subproblem and we only do the same calculation just once and store the result

Memorization -- Caching
Backpack -- box: reuse them past over and over
Memoization is specific way of caching

1. Can be divided into subproble,
2. Recursive Solution
3. Are there repetitive subproblmes?
3. Memoise subporblems
5. Demand a raise from your boss
"""
def addTo80(n):
    print("takes long time")
    return n + 80



def memoization():
    cache = {}
    def innermemoisedAddTo80(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            tmp = n + 80
            cache[n] = tmp
            return cache[n]
    return innermemoisedAddTo80

memoised = memoization()
print(memoised(5))
print(memoised(5))
print(memoised(5))

