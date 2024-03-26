class Solution:
    def removeStars(self, s: str) -> str:
        c = 0
        ans = ''
        for i in s[::-1]:
            if i == '*':
                c += 1
            else:
                if c == 0:
                    ans = i + ans
                else:
                    c -= 1
        return ans
