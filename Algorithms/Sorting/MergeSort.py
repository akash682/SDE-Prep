"""
Divide & Conquer 
This will allow us to make the sorting faster!!
Divide into part and merge it one by one!

Stable: If we have the same value say 6,6 it doesn't change the order
"""

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def mergeSort(array):
    if(len(array)==1):
        return array
    
    # Split array in into right and left
    idx = int(len(array)/2)
    left = array[:idx]
    right = array[idx:]

    print('left:', left)
    print('right', right)

    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if leftIndex == len(left):
        result.extend(right[rightIndex:])
    else:
        result.extend(left[leftIndex:])
    return result
        
ans = mergeSort(numbers)
print(ans)

