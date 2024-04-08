1260. Shift 2D Grid

Easy
Topics
Companies

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].

Element at grid[i][n - 1] moves to grid[i + 1][0].

Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

 

Example 1:

![e1](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/16c83afc-fab2-44be-8385-7a846b596795)


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1

Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

![e2](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/881d8a60-e745-4a3b-9bf5-22038d10ff3a)

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4

Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9

Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length

n == grid[i].length

1 <= m <= 50

1 <= n <= 50

-1000 <= grid[i][j] <= 1000

0 <= k <= 100
