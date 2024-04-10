class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        s = list(s)
        if len(s) == 1:
            return s
        counts = []
        for i in s:
            counts.append(nums.count(i))
        res = []
        for i in range(k):
            m = s[counts.index(max(counts))]
            res.append(m)
            if s: s.remove(m)
            if count: counts.remove(max(counts))
        return res
