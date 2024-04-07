class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMax*n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax, curMin)
        return res
