class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for x in range(n//2, n):
            n1 = (1 + x)*(x/2)
            n2 = (x + n)*((n-x+1)/2)
            if n1 == n2:
                return x
        else:
            return -1
