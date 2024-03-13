from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            if log(n,4) == int(log(n,4)):
                return True
            else:
                return False
        else:
            return False
