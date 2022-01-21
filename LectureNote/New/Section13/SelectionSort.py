"""
Scanning the list and look for minimum and swap with the first item
"""

def SelectionSort(arr):
    for i in range(len(arr)):
        tmpindex = i
        for j in range(i+1, len(arr)):
            if arr[tmpindex] >= arr[j]:
                tmpindex = j
        tmp = arr[i]
        arr[i] = arr[tmpindex]
        arr[tmpindex] = tmp
    return arr


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(SelectionSort(arr))