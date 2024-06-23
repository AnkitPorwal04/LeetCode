class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0 : return 0 
        j = 0
        maxlen = 1
        for i in range(1,len(nums)):
            for k in range(i-1,j-1,-1):
                if nums[i] == nums[k]:
                    break
                if abs(nums[k] - nums[i]) > limit:
                    j = k+1
                    break
            maxlen = max(i-j+1,maxlen)
        return maxlen  
