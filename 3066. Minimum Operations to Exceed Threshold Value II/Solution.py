import bisect
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        while nums and nums[0] < k :
            x, y = nums.pop(0), nums.pop(0)
            new = min(x, y) * 2 + max(x, y)
            bisect.insort_left(nums,new)
            ans += 1
        return ans
