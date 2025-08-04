class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c = Counter()
        res = j = 0
        for i, x in enumerate(fruits):
            c[x] += 1
            while len(c) > 2:
                y = fruits[j]
                c[y] -= 1
                if c[y] == 0:
                    c.pop(y)
                j += 1
            res = max(res, i - j + 1)
        return res
