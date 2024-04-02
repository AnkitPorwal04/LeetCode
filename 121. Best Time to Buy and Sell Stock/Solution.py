class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 #2 pointers!
        while r<len(prices):
            if prices[l]<prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r #we have to shift it to the minimum!
            r += 1
        return max_profit
