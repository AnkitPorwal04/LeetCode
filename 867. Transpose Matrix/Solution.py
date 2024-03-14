class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            l = []
            for j in range(len(matrix)):
                a = matrix[j][i]
                l.append(a)
            ans.append(l)
        return ans
