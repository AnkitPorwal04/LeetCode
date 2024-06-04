class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        if n<5:
            return res
        div = 5
        while True:
            if div>n:
                return res
            res += n//div
            div *= 5
