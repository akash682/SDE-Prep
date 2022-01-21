"""
MergeSort: We divide into pieces and compare the elements and merge set by set
MergeSort is stable which keeps the relative order of the original array.
Best O(nlogn)
Space Complexity is O(n)
"""

def MergeSort(arr):
    if len(arr) == 1:
        return arr

    length_arr = len(arr)
    half_length = int(length_arr/2)

    left = arr[:half_length]
    right = arr[half_length:]
    print("left:", left, "right", right)
    
    return merge(
        MergeSort(left),
        MergeSort(right)
    )

def merge(left, right):
    res_arr = []
    while left or right:
        if not left:
            res_arr.extend(right)
            right = []
        elif not right:
            res_arr.extend(left)
            left = []
        elif left[0] < right[0]:
            res_arr.append(left.pop(0))
        elif left[0] >= right[0]:
            res_arr.append(right.pop(0))
    return res_arr

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(MergeSort(arr))