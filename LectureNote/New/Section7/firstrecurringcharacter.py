def firstRecurringCharacter(arr):
    # Hash Tables O(n)
    hash_set = set()
    for i in range(len(arr)):
        if arr[i] in hash_set:
            return arr[i]
        else:
            hash_set.add(arr[i])
        
    return False

def firstRecurringCharacter_BruteForce(arr):
    # Brute Force O(n^2)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return False

print(firstRecurringCharacter([1,2,3,4,1]))
print(firstRecurringCharacter([2,2,3,4,4]))
print(firstRecurringCharacter([1,2,3,4]))

print(firstRecurringCharacter_BruteForce([1,2,3,4,1]))
print(firstRecurringCharacter_BruteForce([2,2,3,4,4]))
print(firstRecurringCharacter_BruteForce([1,2,3,4]))