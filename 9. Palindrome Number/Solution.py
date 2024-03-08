class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = 0
        x_temp = x
        while x_temp>0:
            rev_x = rev_x*10 + (x_temp%10)
            x_temp //= 10
        if x == rev_x:
            return True
        else:
            return False
