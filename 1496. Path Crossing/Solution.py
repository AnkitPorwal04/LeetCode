class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = [[0,0]]
        x = 0
        y = 0
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == "W":
                x -= 1
            elif i == 'S':
                y -= 1
            if [x,y] not in visited:
                visited.append([x,y])
            else:
                return True
        else:
            return False          
