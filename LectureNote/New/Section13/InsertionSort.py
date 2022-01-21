"""
Insertion Sort gives us the good performation O(n) if it's nearly sorted, samll data sets
"""

def InsertionSort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[i-j-1]:
                if i-j-1 == 0:
                    tmp = arr.pop(i)
                    arr.insert(0, tmp)
            else:
                tmp = arr.pop(i)
                arr.insert(i-j, tmp)
                break
    return arr


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(InsertionSort(arr))

