
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        res = []
        cur_row, cur_col = 0, 0
        going_up = True

        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                going_up = False
            else:
                while cur_row < rows and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    cur_col -= 1
                    cur_row += 1
                if cur_row == rows:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                going_up = True

        return res
