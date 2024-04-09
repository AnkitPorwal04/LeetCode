class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        #remember the divisibility rule of 9
        r = num%9
        if r == 0: 
            return 9
        else: 
            return r
