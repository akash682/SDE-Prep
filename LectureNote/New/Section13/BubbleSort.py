def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] >= arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(BubbleSort(arr))
