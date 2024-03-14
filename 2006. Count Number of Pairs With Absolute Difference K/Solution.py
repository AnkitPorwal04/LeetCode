class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    c += 1
        return c
