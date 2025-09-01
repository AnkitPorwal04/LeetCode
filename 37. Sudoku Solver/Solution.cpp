class Solution {
public:
   bool solveSudoku(vector<vector<char>>& board) {
        return solve(board);
        
    }


    bool solve(vector<vector<char>>& board)
    {
        for(int i = 0;i<board.size();i++)
        {
            for (int j = 0; j<board[0].size();j++)
            {
                // Check for empty cell.
                if(board[i][j] == '.') 
                { 
                  // If an empty cell is found, check for the character that is valid to enter.
                    for(char c = '1'; c <= '9'; c++)
                    {
                        if(isValid(board, i, j , c))
                        {
                            board[i][j] = c;
                            // Check if the valid character allows the sudoku to get solved
                            if(solve(board) == true)
                            {
                                return true;
                            }
                            else
                            {
                                board[i][j] = '.';
                            }
                        }
                        

                    }
                    return false;
                }
                
            }
        }
        return true;
    }

    bool isValid(vector<vector<char>> &board, int row, int col, char c)
    {
      // Checking the validity of the character.
        for(int i=0;i<9;i++)
        {
          // If the character already present in the given row, return false.
            if(board[i][col]==c) return false;
         // If the character already present in the given col, return false.
            if(board[row][i]==c) return false;
        //  If the character is already present in the given grid, return false.
            if(board[3* (row/3) + i/3][3* (col/3) + i%3]==c) return false;

        }
        return true;
    }
};
