class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        maxv = 0
        l = c = 0
        for r in range(len(s)):
            c += 1 if s[r] in vowels else 0
            if r-l+1>k:
                c -= 1 if s[l] in vowels else 0
                l += 1
            maxv = max(maxv, c)
        return maxv
