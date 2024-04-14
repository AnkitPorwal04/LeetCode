class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        s, res = [], 0
        for c in nums:
            while len(s) and s[-1][0] < c: s.pop()
            if len(s) == 0 or s[-1][0] > c: s.append([c, 0])
            s[-1][1] += 1
            res += s[-1][1]
        return res
