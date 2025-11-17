class Solution:
    def numSub(self, s: str) -> int:
        con = 0
        res = 0
        for i in s:
            if i == '1':
                con += 1
                res += con
            else:
                con = 0
        return res%(10**9 + 7)
