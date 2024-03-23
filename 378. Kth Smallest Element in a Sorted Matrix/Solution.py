class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # if  k % len(matrix) != 0:
        #     n = k // len(matrix)
        #     m = k % len(matrix) - 1
        # else:
        #     n = k // len(matrix) - 1
        #     m = len(matrix) - 1
        # return matrix[n][m]
        l = []
        for i in matrix:
            l += i
        l.sort()
        return l[k-1]
