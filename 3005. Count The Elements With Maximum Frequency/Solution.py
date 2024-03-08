class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        n = 0
        for i in num_set:
            if nums.count(i)>max_count:
                max_count = nums.count(i)
                n = 1
            elif nums.count(i)==max_count:
                n+=1
        return n*max_count
