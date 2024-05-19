class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            left_excess = traverse(node.left)
            right_excess = traverse(node.right)
            total_excess = node.val + left_excess + right_excess - 1
            self.moves += abs(total_excess)
            return total_excess

        self.moves = 0
        traverse(root)
        return self.moves
