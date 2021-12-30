"""
Google Question
Given an array = [2,5,1,2,3,4,1,2,3]:
It shoud return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return undefined
"""
def first_recur(arr1):
    count = set ()
    for i in range(len(arr1)):
        if arr1[i] not in count:
            count.add(arr1[i])
        else:
            return arr1[i]
    return False
            

ex1 = [2,5,1,2,3,4,1,2,3]
ex2 = [2,1,1,2,3,5,1,2,4]
ex3 = [2,3,4,5]

print(first_recur(ex1))
print(first_recur(ex2))
print(first_recur(ex3))