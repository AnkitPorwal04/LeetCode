class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        min_num = float('inf')
        count = 0
        for i in matrix:
            for j in i:
                if j <= 0:
                    min_num = min(min_num, -j)
                    res -= j
                    count += 1
                else:
                    min_num = min(min_num, j)
                    res += j
        if count%2 != 0:
            res -= (min_num * 2)
        return res
