class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # let's break n in two parts: (x, n-x)
        # we will start from x == 1
        x = 1
        ans = []
        while True:
            # we will check if there is '0' in any of x and n-x
            # if yes we will update the value in the pair by updating x
            if '0' in str(n-x) or '0' in str(x):
                x += 1
            # else we will update the answer and will come out of the loop
            else:
                ans.append(x)
                ans.append(n-x)
                break
        return ans
