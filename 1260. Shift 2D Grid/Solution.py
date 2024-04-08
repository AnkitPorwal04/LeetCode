class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nr = len(grid)
        nc = len(grid[0])
        res = [0] * nr * nc
        
        k = k % (nr * nc)  

        for i in range(nr):
            for j in range(nc):
                res[i * nc + j] = grid[i][j]
	
        res = res[-k:] + res[:-k]

        for i in range(nr):
            for j in range(nc):
                grid[i][j] = res[i * nc + j]
        return grid
