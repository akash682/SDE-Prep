def reverse(string):
    result = ''
    for i in range(len(string)):
        result += string[len(string)-1-i]
    
    return result

print(reverse("ierdnA si eman vM iH"))

def mergeSortedArrays(arr1, arr2):
    result = [0]*(len(arr1)+len(arr2))
    i = 0
    n = 0
    m = 0
    while True:
        if n == len(arr1):
            result[i] = arr2[m]
            break
        elif m == len(arr2):
            result[i] = arr1[n]
            break

        if arr1[n] <= arr2[m]:
            result[i] = arr1[n]
            n += 1
        else:
            result[i] = arr2[m]
            m += 1
        
        i += 1
    
    return result

result = mergeSortedArrays([0,3,4,31], [4,6,30])
print(result)