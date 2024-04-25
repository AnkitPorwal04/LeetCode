class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*(27+k)
        for i in s:
            val=ord(i)-96+k
            dp[val]=max(dp[val-k:val+k+1])+1
        return max(dp)
