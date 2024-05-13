class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n : return -1
        if d == n : return sum(jobDifficulty)

        @cache
        def recur(i : int, days : int, maxVal : int) :
            if i == n and days == 0: return 0
            if i == n or days == 0: return 9e9
            # Update the maximum difficulty encountered so far.
            maxVal = max(maxVal, jobDifficulty[i]) 
            return min(maxVal + recur(i + 1, days - 1, 0), recur(i + 1, days, maxVal))
        
        return recur(0, d, 0)
