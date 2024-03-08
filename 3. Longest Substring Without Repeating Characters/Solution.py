class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        for i in range(len(s)):
            st = ''
            for j in range(i, len(s)):
                if s[j] not in st:
                    st += s[j]
                else:
                    break
            max_l = max(max_l, len(st))
        return max_l
