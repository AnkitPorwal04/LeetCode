class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ans = []
        for i in nums:
            sum += i
            ans.append(sum)
        return ans
