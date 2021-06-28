"""
Find the minimum/maximum and place it in the left most of the array.
Average O(n^2) Worst O(n^2)
"""
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(numbers)):
        min = 99999
        for j in range(i, len(numbers)):
            if numbers[j] < min:
                min = numbers[j]
                index = j
        tmp = numbers[i]
        numbers[i] = min
        numbers[index] = tmp
    return numbers
print(selectionSort(numbers))