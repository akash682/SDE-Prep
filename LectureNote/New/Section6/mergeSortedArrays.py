def mergeSortedArrays(arr1,arr2):
    result = []
    i = 0
    j = 0
    arr1_tmp = arr1[0]
    arr2_tmp = arr2[0]

    while arr1_tmp or arr2_tmp:
        if not arr2_tmp or arr1_tmp < arr2_tmp:
            result.append(arr1_tmp)
            try:
                arr1_tmp = arr1[i]
            except:
                arr1_tmp = None
            i +=1 
        else: 
            result.append(arr2_tmp)
            try:
                arr2_tmp = arr2[j]
            except:
                arr2_tmp = None
            j +=1

    return result


print(mergeSortedArrays([0,3,4,31], [4,6,30]))