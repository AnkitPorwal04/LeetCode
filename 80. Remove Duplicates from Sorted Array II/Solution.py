class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        for i in s:
            appear = nums.count(i)
            if appear>2:
                while appear != 2:
                    nums.remove(i)
                    appear -= 1
        return len(nums)
