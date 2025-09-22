class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numset = set(nums)
        max_freq = 0
        times = 1
        for i in numset:
            freq = nums.count(i)
            if max_freq == freq:
                times += 1
            elif max_freq < freq:
                max_freq = freq
                times = 1
        return max_freq * times
