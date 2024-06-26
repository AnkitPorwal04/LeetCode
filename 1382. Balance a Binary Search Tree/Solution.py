class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        inorder_traversal = []
        self.inorder(root, inorder_traversal)
        return self.solve(inorder_traversal, 0, len(inorder_traversal) - 1)

    def inorder(self, root: TreeNode, nodes: list) -> None:
        if root is None:
            return
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def solve(self, nodes: list, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.solve(nodes, start, mid - 1)
        root.right = self.solve(nodes, mid + 1, end)
        return root
