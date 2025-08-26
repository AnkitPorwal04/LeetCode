class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        diag = 0
        area = 0
        for i in range(len(dim)):
            d = (dim[i][0]*dim[i][0] + dim[i][1]*dim[i][1])
            a = dim[i][0] * dim[i][1]
            if d > diag or (d == diag and a > area):
                diag = d
                area = a
        return area
