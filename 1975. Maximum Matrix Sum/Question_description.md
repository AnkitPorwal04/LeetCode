1975. Maximum Matrix Sum

You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:

<img width="401" height="81" alt="image" src="https://github.com/user-attachments/assets/b80bcd71-485a-4b44-b7d5-10ba7448fba7" />


Input: matrix = [[1,-1],[-1,1]]

Output: 4

Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

  
Example 2:

<img width="321" height="121" alt="image" src="https://github.com/user-attachments/assets/a89e279a-3bb0-4957-87c7-2050e7aa03b1" />


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]

Output: 16

Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

- n == matrix.length == matrix[i].length
- 2 <= n <= 250
- -105 <= matrix[i][j] <= 105
