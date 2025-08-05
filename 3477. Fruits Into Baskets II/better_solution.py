#this solution has a better time complexity

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        n = len(baskets)
        for fruit in fruits:
            c = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    c = 0
                    break
            count += c
        return count
