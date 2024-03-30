class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        else:
            num = 1
            ans = 1
            while num%k != 0:
                num = 10*num+1
                ans += 1
            return ans
