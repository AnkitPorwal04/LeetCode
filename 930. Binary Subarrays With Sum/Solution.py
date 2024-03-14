class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # c = 0
        # for i in range(len(nums)):
        #     s = nums[i]
        #     if s==goal:
        #         c = c + 1
        #     if i+1<len(nums):
        #         for j in range(i+1, len(nums)):
        #             s = s + nums[j]
        #             if s == goal:
        #                 c = c+1
        # return c
        dic = {0: 1}
        curr_sum = 0
        count = 0

        for i in nums:
            curr_sum += i
            if curr_sum - goal in dic:
                count += dic[curr_sum - goal]
            dic[curr_sum] = dic.get(curr_sum, 0) + 1
        return count
