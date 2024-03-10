class Solution:
    def reverse(self, x: int) -> int:
        # x_rev = 0
        # temp = abs(x) 
        # while temp:
        #     n = temp%10
        #     x_rev = x_rev*10 + n
        #     temp //= 10
        # if x<0:
        #     x_rev = 0 - x_rev
        # if x_rev>=-2**31 and x_rev<2**31:
        #     return x_rev
        # else:
        #     return 0
        xrev = int(str(abs(x))[::-1])
        if x<0:
            xrev = -xrev
        if xrev>=-2**31 and xrev<2**31:
            return xrev
        else:
            return 0
