class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        minimum=maximum=nonelement=-1
        for ind,val in enumerate(nums):
            if val==minK:
                minimum=ind
            if val==maxK:
                maximum=ind
            if not minK<=val<=maxK:
                nonelement=ind
            count+=max(0,min(minimum,maximum)-nonelement)
        return count
