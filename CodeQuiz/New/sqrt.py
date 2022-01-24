import sqlite3
class Solution:
    def mySqrt(self, x):
        i = 0
        while i**2 < x:
            i += 1
        return i