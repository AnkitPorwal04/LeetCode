class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumTotal = 0

        for num in nums:
            sumTotal |= num
        return sumTotal << (len(nums) - 1)
