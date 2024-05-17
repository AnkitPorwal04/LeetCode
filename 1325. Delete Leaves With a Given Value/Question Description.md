1325. Delete Leaves With a Given Value

Medium
Topics
Companies

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:

![sample_1_1684](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/03cd7c18-ba1a-4f3d-bc5f-bba906ff2b40)

- Input: root = [1,2,3,2,null,2,4], target = 2
- Output: [1,null,3,null,4]
- Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:

![sample_2_1684](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/f0f61811-5f8c-4f1f-bac8-4c3859e908b5)

- Input: root = [1,3,3,3,2], target = 3
- Output: [1,3,null,null,2]

Example 3:

![sample_3_1684](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/fbde4a90-6ce9-4908-8998-4b75f6ea8ed2)

- Input: root = [1,2,null,2,null,2], target = 2
- Output: [1]
- Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

- The number of nodes in the tree is in the range [1, 3000].
- 1 <= Node.val, target <= 1000
