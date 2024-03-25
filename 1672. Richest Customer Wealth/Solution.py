class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            ans = max(sum(i), ans)
        return ans
