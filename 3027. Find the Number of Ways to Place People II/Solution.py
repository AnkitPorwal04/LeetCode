class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)

        # Sort by x ascending, and if x is the same, y descending
        points.sort(key=lambda p: (p[0], -p[1]))

        result = 0

        for i in range(n):
            x1, y1 = points[i]
            bestY = float("-inf")

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Must be "lower-right": y2 ≤ y1
                if y2 > y1:
                    continue

                if y2 > bestY:
                    result += 1
                    bestY = y2

        return result
