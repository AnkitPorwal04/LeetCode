class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        def dfs_helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs_helper(i-1, j)
                dfs_helper(i+1, j)
                dfs_helper(i, j-1)
                dfs_helper(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs_helper(i, j)
        return res
        
