class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        def solve(nums: List[int], k: int) -> int:
            ans = 0
            n = len(nums)
            cnt = defaultdict(int)
            diff = 0

            l = 0
            for r in range(n):
                cnt[nums[r]] += 1
                if cnt[nums[r]] == 1:
                    diff += 1

                while diff > k:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        diff -= 1
                    l += 1
                ans += (r - l + 1)
            return ans
        
        return solve(nums, k) - solve(nums, k - 1)
        
        # c = 0
        # for i in range(len(nums)):
        #     arr = []
        #     for j in range(i, len(nums)):
        #         arr.append(nums[j])
        #         if len(set(arr)) == k:
        #             c += 1
        # return c
        
