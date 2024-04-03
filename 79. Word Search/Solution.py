class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        NROWS = len(board)
        NCOLS = len(board[0])
        N = len(word)
        DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

        # To improve efficiency. If char not found in board, can return False immediately without running through backtrack
        board_charset = set()
        for r in range(NROWS):
            for c in range(NCOLS):
                board_charset.add(board[r][c])
        for char in word:
            if char not in board_charset:
                return False

        def backtrack(r, c, idx, seen=set()):
            if (0 <= r < NROWS and 
                0 <= c < NCOLS and
                (r,c) not in seen and
                board[r][c] == word[idx]):

                # found match
                if idx == N-1:
                    return True
                seen.add((r,c))
                for dr, dc in DIRS:
                    if backtrack(r+dr,c+dc,idx+1,seen):
                        return True
                seen.remove((r,c))
                
        for r in range(NROWS):
            for c in range(NCOLS):
                if backtrack(r,c,0):
                    return True
        return False
