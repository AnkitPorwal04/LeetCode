143. Reorder List

Medium Topics Companies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 
Example 1:

![reorder1linked-list](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/dd63b225-0a1a-4a92-afbe-442d8bc2073b)

Input: head = [1,2,3,4]

Output: [1,4,2,3]

Example 2:
![reorder2-linked-list](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/c1ec435d-52ce-45aa-b4c7-9e016c8afd7d)

Input: head = [1,2,3,4,5]

Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].

1 <= Node.val <= 1000
