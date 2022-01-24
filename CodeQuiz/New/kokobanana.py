class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            m = int((l + r)/2)
            if sum(int((p-1)/m)+1 for p in piles) > h:
                l = m+1
            else:
                r = m
        return l