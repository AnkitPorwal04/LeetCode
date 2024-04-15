class Solution:
    def partitionString(self, s: str) -> int:
        c, l = 0, 0
        ss = ''
        for r in range(len(s)):
            if s[r] not in ss:
                ss += s[r]
            else:
                c += 1
                ss = s[r]
        return c+1
