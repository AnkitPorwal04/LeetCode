class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += '0' if i%2 else '1'
            alt2 += '1' if i%2 else '0' 
        res = len(s)
        dif1, dif2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                dif1 += 1
            if s[r] != alt2[r]:
                dif2 += 1
            
            if(r-l+1) > n:
                if s[l] != alt1[l]:
                    dif1 -= 1
                if s[l] != alt2[l]:
                    dif2 -= 1
                l += 1
            
            if (r-l+1) == n:
                res = min(res, dif1, dif2)
        return res
