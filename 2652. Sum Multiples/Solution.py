class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        while n:
            if n%3 == 0 or n%5 == 0 or n%7 == 0:
                ans += n
            n -= 1
        return ans
