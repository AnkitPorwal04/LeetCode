class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return ((nums.pop(nums.index(max(nums)))) - 1) * ((nums.pop(nums.index(max(nums)))) - 1)
