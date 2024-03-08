class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            l = [1,1]
            for j in range(2, i+1):
                l.insert(j-1, (pascal[-1][j-1]+pascal[-1][j-2]))
            pascal.append(l)
        return pascal[rowIndex]
