class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float("inf")
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                size = min(size, (r-l+1))
                total -= nums[l]
                l += 1
            

        return 0 if size == float("inf") else size
