class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        for i in nums:
            arr[i] += 1
        res = []
        for i in range(len(arr)):
            if arr[i] == 2:
                res.append(i)
        return res
