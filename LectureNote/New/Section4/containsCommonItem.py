arr1 = ['a', 'b', 'c', 'd']
arr2 = ['z', 'y', 'w']

def containsCommonItem(arr1, arr2):
    for i in range (len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


def containsCommonItem2(arr1, arr2):
    hash_seen = {}
    for i in range(len(arr1)):
        if arr1[i] not in hash_seen:
            hash_seen[arr1[i]] = True

    for j in range(len(arr2)):
        if arr2[j] in hash_seen:
            return True
        return False

