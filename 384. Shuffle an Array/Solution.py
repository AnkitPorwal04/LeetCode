class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.perm_nums = list(nums)

    def reset(self) -> List[int]:
        return self.perm_nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
