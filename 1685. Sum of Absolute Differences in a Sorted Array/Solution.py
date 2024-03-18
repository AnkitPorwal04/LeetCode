class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Calculate the prefix sum (cumulative sum from the start)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        total_sum = prefix_sum[n]  # Total sum of the array
        result = []
        for i in range(n):
            # Sum of absolute differences for nums[i]
            # For elements to the left of i: nums[i] * i - prefix_sum[i]
            # For elements to the right of i: (prefix_sum[n] - prefix_sum[i + 1]) - nums[i] * (n - i - 1)
            left_sum = nums[i] * i - prefix_sum[i]
            right_sum = (total_sum - prefix_sum[i + 1]) - nums[i] * (n - i - 1)
            result.append(left_sum + right_sum)
        
        return result
