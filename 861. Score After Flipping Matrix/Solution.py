class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = (1 << (m - 1)) * n

        for j in range(1, m):
            val = 1 << (m - 1 - j)
            set_count = 0

            for i in range(n):
                if grid[i][j] == grid[i][0]:
                    set_count += 1

            res += max(set_count, n - set_count) * val

        return res
