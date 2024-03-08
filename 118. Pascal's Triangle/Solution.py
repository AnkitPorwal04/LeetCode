class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1,1]]
        for i in range(2, numRows):
            l = [1,1]
            for j in range(2, i+1):
                l.insert(j-1, (pascal[-1][j-1]+pascal[-1][j-2]))
            pascal.append(l)
        if numRows>1: 
            return pascal 
        else:
            return [[1]]
