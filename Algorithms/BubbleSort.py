numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4 ,0]

def bubbleSort(array):
    for itr in range(len(numbers)):
        for i in range(len(numbers)-1-itr):
            if numbers[i] > numbers[i+1]:
                tmp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = tmp
    
    return numbers


print(bubbleSort(numbers))
