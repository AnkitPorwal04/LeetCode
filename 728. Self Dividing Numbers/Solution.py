class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            flag = True
            i_permanent = i
            while i:
                divisor = i%10
                if divisor==0:
                    flag = False
                    break
                elif i_permanent%divisor != 0:
                    flag = False
                    break
                i //= 10
            if flag:
                ans.append(i_permanent)
        return ans
