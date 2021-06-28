"""
Insertion Sort is best when performing small dataset and nearly sorted datasets.
"""
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(len(array)):
        for j in range(i-1):
            if array[i] < array[j]:
                tmp = array.pop(i)
                array.insert(j, tmp)
                break
    return array

print(insertionSort(numbers))
