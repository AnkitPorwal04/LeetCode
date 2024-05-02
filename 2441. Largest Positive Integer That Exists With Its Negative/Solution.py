# class Solution:
#    def findMaxK(self, nums: List[int]) -> int:
#        ans = -1
#        nums.sort()
#        while nums:
#            if -(nums[-1]) in nums:
#                ans = nums[-1]
#                break
#            else:
#                nums.remove(nums[-1])
#        return ans
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        nums.sort()
        i = len(nums)-1
        while nums and nums[i]>0:
            if -(nums[i]) in nums:
                ans = nums[i]
                break
            else:
                nums.remove(nums[-1])
            i -= 1
        return ans
