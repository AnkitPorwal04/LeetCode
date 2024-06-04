class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l,r= 0, 1
        while l < len(nums):
            if r<len(nums) and nums[r] == nums[r-1]+1:
                r += 1
            else:
                if r - 1 == l:
                    res.append(str(nums[l]))
                else:
                    res.append(str(nums[l]) + "->" + str(nums[r-1]))
                l = r
                r += 1
        return res
