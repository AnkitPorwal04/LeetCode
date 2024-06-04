class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set(s)
        hm = {}
        for i in set_s:
            hm[i] = s.count(i)
        ans = 0
        maxodd = 0
        for j in hm.values():
            if j%2 == 0:
                ans += j
            else:
                ans += j-1
        if ans == len(s):
            return ans
        else:
            return ans + 1
