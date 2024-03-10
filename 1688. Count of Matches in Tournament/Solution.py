class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n>1:
            m += n//2
            if n%2 != 0:
                n = n//2 + 1
            else:
                n = n//2
        return m
