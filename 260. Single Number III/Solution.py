class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []
        for i in s:
            if nums.count(i)==1:
                res.append(i)
        return res
