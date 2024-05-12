class Solution:
    def maxScore(self, s: str) -> int:
        maxcount = 0
        for i in range(len(s)-1):
            z = s[:i+1].count('0')
            o = s[i+1:].count('1')
            maxcount = max(maxcount,(z+o))
        return maxcount
