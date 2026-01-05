class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            divisors = set()
            n = int(sqrt(i) + 1)
            for j in range(1, n):
                if i%j == 0:
                    divisors.add(j)
                    divisors.add(i//j)
            if len(divisors) == 4:
                res += sum(divisors)
        return res
