class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        ans = nb
        while nb>=ne:
            ans += nb//ne
            nb = nb//ne + nb%ne
        return ans
        
