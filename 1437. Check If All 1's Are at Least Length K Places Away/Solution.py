class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                n = min(i+k+1, len(nums))
                for j in range(i+1, n):
                    if nums[j] == 1:
                        return False
        else:
            return True
