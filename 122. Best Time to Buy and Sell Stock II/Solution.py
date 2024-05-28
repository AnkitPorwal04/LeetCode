class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we'll just iterate throug the array and consider each and every profit we're
        # making by subtractinf higher value from lower value.
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
