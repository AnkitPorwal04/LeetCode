import math as m
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    num = m.sqrt((i+1)**2 + (j+1)**2)
                    if num <= n and num >= 1 and num == int(num):
                        count += 1
        return count
