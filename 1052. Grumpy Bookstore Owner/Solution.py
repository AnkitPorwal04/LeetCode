class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        total = sum((1 - grumpy[i]) * customers[i] for i in range(len(customers)))

        window_all = 0
        window_partial = 0
        for i in range(len(customers)):
            window_all += customers[i]
            window_partial += (1 - grumpy[i]) * customers[i]
            if i + 1 >= minutes:
                ans = max(ans, total - window_partial + window_all)
                left = i - minutes + 1
                window_all -= customers[left]
                window_partial -= (1 - grumpy[left]) * customers[left]

        return ans
