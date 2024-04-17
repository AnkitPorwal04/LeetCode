988. Smallest String Starting From Leaf

Medium
Topics
Companies

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 
Example 1:

![tree1](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/ec7566ca-f5b6-4ea5-bc07-23ac227d4746)

Input: root = [0,1,2,3,4,3,4]

Output: "dba"

Example 2:

![tree2](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/bf8d6fb4-fb59-40c1-8062-68cee2c2a622)

Input: root = [25,1,3,1,3,0,2]

Output: "adz"

Example 3:

![tree3](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/c03efc97-cc88-419e-aae2-4eab78ed9f22)

Input: root = [2,2,1,null,1,0,null,0]

Output: "abc"
 

Constraints:

The number of nodes in the tree is in the range [1, 8500].

0 <= Node.val <= 25
