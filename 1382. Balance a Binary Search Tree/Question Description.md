1382. Balance a Binary Search Tree

Medium
Topics
Companies

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

![balance1-tree](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/877b4ec5-2d29-40f8-9d11-8615f6fab1a1)

- Input: root = [1,null,2,null,3,null,4,null,null]
- Output: [2,1,3,null,null,null,4]
- Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.


Example 2:

- Input: root = [2,1,3]
- Output: [2,1,3]
 

Constraints:

- The number of nodes in the tree is in the range [1, 104].
- 1 <= Node.val <= 105
