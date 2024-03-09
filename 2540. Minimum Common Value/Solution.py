class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1)<min(nums2) or max(nums2)<min(nums1):
            return -1
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    return i
            else:
                return -1
        else:
            for i in nums2:
                if i in nums1:
                    return i
            else:
                return -1
