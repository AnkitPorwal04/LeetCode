class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = s[0]
        max_len = 1
        for i in range(len(s)-1):
            x = s[i]
            for j in range(i+1, len(s)):
                x += s[j]
                if x == x[::-1] and len(x)>max_len:
                    n = x
                    max_len = len(x)
        return n
