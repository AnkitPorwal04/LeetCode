class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = nums.count(0),nums.count(1),nums.count(2)
        nums[:] = [0]*red + [1]*white + [2]*blue
