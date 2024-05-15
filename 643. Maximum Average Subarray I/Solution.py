class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = maxsumm = sum(nums[:k])

        for i in range(k, len(nums)):
            summ += nums[i] - nums[i-k]
            maxsumm = max(maxsumm, summ)
        return maxsumm/k
