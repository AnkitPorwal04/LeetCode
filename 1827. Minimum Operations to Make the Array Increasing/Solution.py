class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        count = prev= 0
        for i in nums:
            if i <= prev :
                prev += 1
                count += prev-i
            else:
                prev = i
        return count
