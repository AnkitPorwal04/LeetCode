class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        f = fruits.copy()
        for i in range (len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets.pop(j)
                    f.remove(fruits[i])
                    break
        return len(f)
