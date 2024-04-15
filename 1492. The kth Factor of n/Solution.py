class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        r = int(math.sqrt(n)) + 1
        factors = []
        for i in range(1, r):
            if n%i == 0:
                factors.append(i)
                if n//i not in factors: factors.append(n//i)
        factors.sort()
        return factors[k-1] if len(factors)>=k else -1
