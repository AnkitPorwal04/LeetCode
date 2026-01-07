1339. Maximum Product of Splitted Binary Tree

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:

<img width="695" height="232" alt="image" src="https://github.com/user-attachments/assets/ac6b508a-108d-4f19-ba44-366555092dd6" />

- Input: root = [1,2,3,4,5,6]
- Output: 110
- Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

<img width="667" height="281" alt="image" src="https://github.com/user-attachments/assets/b34eb802-ef95-44f5-ad88-693577848c95" />

- Input: root = [1,null,2,3,4,null,null,5,6]
- Output: 90
- Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

- The number of nodes in the tree is in the range [2, 5 * 104].
- 1 <= Node.val <= 104
