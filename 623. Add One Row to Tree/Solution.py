# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(root, val, depth):
            if root==None: return
            if depth>2:
                dfs(root.left, val, depth-1)
                dfs(root.right, val, depth-1)
            else:
                ptr=root.left
                root.left=TreeNode(val, ptr, None)

                ptr=root.right
                root.right=TreeNode(val, None, ptr)
        if depth==1:
            ptr=TreeNode(val, root, None)
            return ptr
        dfs(root, val, depth)
        return root
