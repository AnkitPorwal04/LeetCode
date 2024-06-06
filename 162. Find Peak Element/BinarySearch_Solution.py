class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i+j) // 2

            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid + 1
            

        return i
