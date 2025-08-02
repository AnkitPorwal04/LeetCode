from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        min_val = float('inf')
        balance = {}
        
        # we will traverse both the arrays and increase the frequency by one when in basket1 and decrease by one when found in baasket2, so that already balanced number will get cancelled out and,
        # the ones with uneven composition will have a frequency of even number (+ve for basket1 and -ve for basket2)
        for x, y in zip(basket1, basket2):
            balance[x] = balance.get(x, 0) + 1
            balance[y] = balance.get(y, 0) - 1
            min_val = min(min_val, x, y)
        
        # we will collect those values and store them in an array named transfers, and then we will sort them, and we will be storing them only half the times of their +ve frequency. 
        transfers = []
        for val, bal in sorted(balance.items()):
            if bal == 1:
                return -1  # cannot balance as the frequency is one
            transfers.extend([val] * (abs(bal) // 2))
        
        # Pair the smallest surpluses, that we will take only those number into consideration from the transfer array after sorting, which are lowest, so the technically the first half of the numbers..
        transfers.sort()
        cost = 0
        m = len(transfers)
        for i in range(m // 2):
            cost += min(transfers[i], 2 * min_val)
        
        return cost
