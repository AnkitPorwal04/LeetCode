class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if i>0:
                a = nums.index(i)
                break
        else:
            return 1
        nums = nums[a:]
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
                break
        else:
            return i+2
