310. Minimum Height Trees

Medium
Topics
Companies

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:

![e1](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/8861e281-f212-496b-9f06-ce85916694ce)

Input: n = 4, edges = [[1,0],[1,2],[1,3]]

Output: [1]

Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

![e2](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/3189b0fa-51e3-422d-a3fd-fc384027c3eb)

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

Output: [3,4]
 

Constraints:
```
1 <= n <= 2 * 104
edges.length == n - 1 \n
0 <= ai, bi < n \n
ai != bi \n
All the pairs (ai, bi) are distinct. \n
The given input is guaranteed to be a tree and there will be no repeated edges.
```
