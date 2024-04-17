# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numToal(self, number):
        return chr(ord('a') + number)
        
    def smallestFromLeaf(self, root: TreeNode) -> str:
        queue = collections.deque()
        queue.append((root, self.numToal(root.val)))
        results = []
        
        while queue:
            cur, path = queue.popleft()
            if not cur.left and not cur.right:
                results.append(path[::-1])
            if cur.left:
                queue.append((cur.left, path + self.numToal(cur.left.val)))
            if cur.right:
                queue.append((cur.right, path + self.numToal(cur.right.val)))
        results.sort()
        return results[0]
