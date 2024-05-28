class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        while len(n)!= 1:
            summ = 0
            for i in n:
                summ += int(i)**2
                n = str(summ)
        if n == '1' or n =='7':
            return True
        else:
            return False
