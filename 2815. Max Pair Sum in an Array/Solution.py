class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        l = len(nums)
        for i in range(l-1):
            num1 = max(str(nums[i]))
            for j in range(i+1, l):
                num2 = max(str(nums[j]))
                if num1 == num2:
                    ans = max(ans, nums[i] + nums[j])
        return ans
        
