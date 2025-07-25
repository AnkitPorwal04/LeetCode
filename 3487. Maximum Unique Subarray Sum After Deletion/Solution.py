class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-1, -1, -1):
            if (nums[i]<=0 or nums.count(nums[i])>1) and (len(nums)>1):
                nums.pop(i)
        return sum(nums)
        
