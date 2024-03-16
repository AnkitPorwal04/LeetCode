class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        nums.remove(nums[0])
        nums.remove(nums[0])
        for i in nums:
            if arr1[-1]>arr2[-1]:
                arr1.append(i)
            else:
                arr2.append(i)
        return arr1+arr2
