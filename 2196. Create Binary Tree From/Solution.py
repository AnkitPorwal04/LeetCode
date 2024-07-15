# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root, n= -1, len(descriptions)
        parent={}
        node={}

        for x, y, l in descriptions:
            if x not in node:
                node[x]=TreeNode(x)
                if x not in parent:
                    root=x
            if y not in node:
                node[y]=TreeNode(y)
            parent[y]=x
            if l:
                node[x].left=node[y]
            else:
                node[x].right=node[y]

        while root in parent:
            root=parent[root]

        return node[root]
        
