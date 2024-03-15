from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = [i+1 for i in range(n)]
        return self.solve(k-1, l)

    def solve(self, k, l) -> str:
        n = len(l)
        if n == 1:
            return str(l[0])
        elif k == 0:
            return "".join([str(i) for i in l])
        else:
            x = factorial(n-1)
            i = k//x
            return str(l[i]) + self.solve(k%x, l[:i]+l[i+1:])
