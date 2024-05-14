class Solution:
    roww = [1, -1, 0, 0]
    coll = [0, 0, -1, 1]

    def dfs(self, grid, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0
        
        curr = grid[x][y]
        grid[x][y] = 0
        localMaxGold = curr

        for i in range(4):
            newX = x + self.roww[i]
            newY = y + self.coll[i]
            localMaxGold = max(localMaxGold, curr + self.dfs(grid, newX, newY, n, m))

        grid[x][y] = curr
        return localMaxGold

    def getMaximumGold(self, grid):
        n = len(grid)
        m = len(grid[0])
        maxGold = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid, i, j, n, m))

        return maxGold
