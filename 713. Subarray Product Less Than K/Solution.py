# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         c = 0
#         for i in range(len(nums)):
#             l = 1
#             for j in range(i, len(nums)):
#                 l *= nums[j]
#                 if l<k:
#                     c += 1
#                 else:
#                     break
#         return c

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        count = 0
        prod = 1
        left = 0
        
        for right, num in enumerate(nums):
            prod *= num 
            while prod >= k:  
                prod /= nums[left]
                left += 1
            count += right - left + 1  
        
        return count
        
