class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            c = 0
            for j in nums:
                if j >= i:
                    c += 1
            if c == i:
                return c
        return -1 
