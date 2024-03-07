class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        flag = True
        n = 2**(n-1)
        while n!= 1:
            n //= 2
            if k>n:
                k-=n
                flag = not flag
        return 0 if flag else 1
