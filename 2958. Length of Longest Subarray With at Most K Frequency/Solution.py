class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # maxcount = 0
        # for i in range(len(nums)):
        #     arr = []
        #     for j in range(i, len(nums)):
        #         if arr.count(nums[j]) < k:
        #             arr.append(nums[j])
        #         else:
        #             break
        #     maxcount = max(len(arr), maxcount)
        # return maxcount
        res = 0
        count = defaultdict(int)
        l = 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            while count[nums[i]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res , i - l + 1)
        return res     
