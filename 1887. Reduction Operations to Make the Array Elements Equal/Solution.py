class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        ans=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                ans+=i+1
        return ans         

        # nums.sort()
        # res = 0
        # while True:
        #     if len(set(nums)) == 1:
        #         return res
        #     c = nums.count(nums[-1])
        #     idx = nums.index(max(nums))
        #     nums = nums[:idx] + [max(nums[:idx])]*c
        #     res += c
