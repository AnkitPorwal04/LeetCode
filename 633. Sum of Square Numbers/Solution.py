class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i<=j:
            n = i**2 + j**2
            if n == c:
                return True
            elif n>c:
                j -= 1
            elif n<c:
                i += 1
