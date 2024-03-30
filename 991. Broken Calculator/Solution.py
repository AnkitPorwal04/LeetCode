class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0 
        while target > startValue:
            if not target % 2:
                target /= 2
            else:
                target += 1

            ans += 1

        return ans + int(startValue - target)
