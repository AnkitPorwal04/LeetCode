class Solution:
    def countOdds(self, low: int, high: int) -> int:
        r = high-low+1
        if r%2 == 0:
            return r//2
        else:
            extras = 0
            if low%2 != 0:
                extras += 1
                low += 1
            if high%2 != 0:
                extras += 1
                high -= 1
            return (high-low+1)//2 + extras
