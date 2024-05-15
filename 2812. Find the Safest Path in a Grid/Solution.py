class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        nRows, nCols = len(grid), len(grid[0])

        def inBound(row, col):
            return 0 <= row < nRows and 0 <= col < nCols

        def bfs(thievesGrids):
            while thievesGrids:
                for _ in range(len(thievesGrids)):
                    row, col = thievesGrids.popleft()
                    value = grid[row][col]

                    for x, y in directions:
                        newX, newY = x + row, y + col
                        if inBound(newX, newY) and grid[newX][newY] == -1:
                            grid[newX][newY] = value + 1
                            thievesGrids.append((newX, newY))

        def calculateSafeness():
            priorityQueue = [(-grid[0][0], 0, 0)]
            grid[0][0] = -1

            while priorityQueue:
                safeness, row, col = heappop(priorityQueue)

                if (row, col) == (nRows - 1, nCols - 1):
                    return -safeness

                for x, y in directions:
                    newX, newY = x + row, y + col
                    if inBound(newX, newY) and grid[newX][newY] != -1:
                        heappush(priorityQueue, (-min(-safeness,
                                 grid[newX][newY]), newX, newY))
                        grid[newX][newY] = -1

            return -1

        thievesGrids = deque()
        for row in range(nRows):
            for col in range(nCols):
                if grid[row][col] == 1:
                    thievesGrids.append((row, col))
                    # Mark thief cell with 0
                    grid[row][col] = 0
                else:
                    # Mark empty cell with -1
                    grid[row][col] = -1

        bfs(thievesGrids)
        return calculateSafeness()
