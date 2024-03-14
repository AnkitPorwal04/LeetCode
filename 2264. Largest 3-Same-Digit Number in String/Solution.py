class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = '000'
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if int(num[i:i+3])>int(ans):
                    ans = num[i:i+3]
        if ans == '000' and ans not in num:
            return ''
        else:
            return ans
