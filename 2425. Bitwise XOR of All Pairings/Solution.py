class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        ans1=0
        ans2=0
        for i in range (n2):
            ans2^=nums2[i]
        for i in range (n1):
            ans1^=nums1[i]
        if n1%2==0 and n2%2==0:
            return 0
        elif n1%2==1 and n2%2==0:
            return ans2
        elif n1%2==0 and n2%2==1:
            return ans1
        else:
            return ans1^ans2
            
