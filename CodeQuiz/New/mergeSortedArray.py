def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        nums1[0] = nums2[0]
    elif n == 0:
        pass
    else:
        pointer = 0
        hikaku = nums2.pop(0)
        while True:
            if pointer > m + n:
                nums1[pointer] = hikaku
                nums1[pointer+1: ] = nums2
                break
                
            if hikaku < nums1[pointer]:
                nums1[pointer + 1:pointer + m + 1] = nums1[pointer:pointer+m]
                nums1[pointer] = hikaku
                hikaku = nums2.pop(0)
                pointer += 1
            else:
                pointer += 1
                continue
    
    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [1]
m = 1
nums2 = []
n = 0

nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1,m,nums2,n)