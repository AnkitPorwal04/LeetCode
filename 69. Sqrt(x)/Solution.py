class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        for i in range(x+1):
            if i*i == x: 
                return i
            elif i*i > x:
                return i-1 
