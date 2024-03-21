class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        for i in s:
            if i == 'i':
                ans = ans[::-1]
            else:
                ans += i
        return ans
