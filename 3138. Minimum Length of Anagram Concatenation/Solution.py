class Solution:
    def minAnagramLength(self, s: str) -> int:
        from collections import Counter
        n = len(s)
        frequency = Counter(s)
        for i in range(1, n+1):
            if n % i == 0:
                if all((freq % (n // i) == 0) for freq in frequency.values()):
                    return i
        return n
