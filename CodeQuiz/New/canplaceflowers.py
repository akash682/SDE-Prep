class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n==1:
            return True

        for i in range(len(flowerbed)):            
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[1] == 0:
                        flowerbed[0] = 1
                        n -= 1 
                elif i == len(flowerbed) -1:
                    if flowerbed[len(flowerbed) -2] == 0:
                        flowerbed[len(flowerbed)-1] =1 
                        n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n <= 0:
                return True
        return False
                    