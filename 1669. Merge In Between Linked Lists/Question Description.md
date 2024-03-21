1669. Merge In Between Linked Lists

Medium Topics Companies

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

![fig1](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/e08baa48-bebd-469d-9241-7b71b44752d5)

Build the result list and return its head.

 
Example 1:

![ll](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/56810b06-bb49-4d8c-8f6b-b7b40296f7aa)

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]

Output: [10,1,13,1000000,1000001,1000002,5]

Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:

![merge_linked_list_ex2](https://github.com/AnkitPorwal04/LeetCode/assets/96345105/ba0af5c6-42d2-4b0e-92d5-1232f6302eb5)

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]

Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]

Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 104

1 <= a <= b < list1.length - 1

1 <= list2.length <= 104
