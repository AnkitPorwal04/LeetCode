class Solution:
    def findMinArrowShots(self, points):
        points.sort()
        y = points[0][1]
        ans = 1
        for i in range(1, len(points)):
            if points[i][0] > y:
                ans += 1
                y = points[i][1]
            y = min(points[i][1], y)
        return ans
