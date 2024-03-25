class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums2 = list(nums)
        nums2.sort()
        if nums == nums2 or nums == nums2[::-1]:
            return True
        else:
            return False
