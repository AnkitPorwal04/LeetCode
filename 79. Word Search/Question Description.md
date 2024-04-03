79. Word Search

Medium Topics Companies

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

![word2](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/6a0c3dcd-9a64-47e1-a21b-fec3f0e26be1)


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

Output: true

Example 2:

![word-1](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/e6e06563-4326-4071-ad45-ab44bc18a5e1)


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"

Output: true

Example 3:

![word3](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/00f6c67a-bc5d-475c-a673-e1013dd44654)


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"

Output: false
 

Constraints:

m == board.length

n = board[i].length

1 <= m, n <= 6

1 <= word.length <= 15

board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
