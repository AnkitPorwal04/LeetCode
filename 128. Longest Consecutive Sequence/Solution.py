class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        count = 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                s.add(nums[i])
                s.add(nums[i+1])
            elif nums[i] == nums[i+1]:
                pass
            else:
                count = max(len(s), count)
                s = set()
        count = max(len(s), count)
        return count
