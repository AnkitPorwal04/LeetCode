class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 5:
            return 100 - (purchaseAmount+5)
        n = purchaseAmount/10
        n = round(n)*10
        return 100 - n
