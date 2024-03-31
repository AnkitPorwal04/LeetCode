class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        x = 0
        for i in nums:
            x ^= i
        return x == 0 or len(nums)%2 == 0
