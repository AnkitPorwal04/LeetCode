class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for i in nums:
            for j in range(i[0], i[-1]+1):
                s.add(j)
        return len(s)
