class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        checker = 0
        ans = 0

        for i in nums:
            checker = max(checker, i)
            ans += checker - i
            checker += 1
        return ans
