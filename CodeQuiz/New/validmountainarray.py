class Solution:
    def validMountainArray(self, arr) -> bool:
        inc_flag = True
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                inc_flag = False
            elif arr[i] < arr[i+1]:
                if inc_flag == False:
                    return False  
        
        if inc_flag == True:
            return False
        elif max(arr) == arr[0]:
            return False
        return True