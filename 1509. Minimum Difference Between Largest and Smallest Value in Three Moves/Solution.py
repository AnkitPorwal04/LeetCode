class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        return min(
            nums[-1] - nums[3],    # Remove the three smallest
            nums[-2] - nums[2],    # Remove the two smallest and the largest
            nums[-3] - nums[1],    # Remove the smallest and the two largest
            nums[-4] - nums[0]     # Remove the three largest
        )
