from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None] * n for _ in range(n)]   # memoization table
        return self.helper(triangle, 0, 0, dp)

    def helper(self, triangle: List[List[int]], row: int, col: int, dp: List[List[int]]) -> int:
        if row == len(triangle):
            return 0

        if dp[row][col] is not None:
            return dp[row][col]

        result = triangle[row][col] + min(
            self.helper(triangle, row + 1, col, dp),
            self.helper(triangle, row + 1, col + 1, dp)
        )

        dp[row][col] = result
        return result
