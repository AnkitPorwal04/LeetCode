class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
            for _ in range(2, n):
                ans = t0 + t1 + t2
                t0 = t1
                t1 = t2
                t2 = ans
            return ans
