class Solution:
    def integerReplacement(self, n: int) -> int:
        data = {1:0}
        def dp(num):
            if num == 1:
                return 0
            if num in data:
                return data[num]
            if num % 2 == 0:
                data[num] = 1 + dp(num//2)
            else:
                data[num] = 1 + min(dp(num + 1), dp(num - 1) )
            return data[num]

        res =  dp(n)
        return res
