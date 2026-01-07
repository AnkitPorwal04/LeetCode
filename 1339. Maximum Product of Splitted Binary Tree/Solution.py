class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # compute total sum of the tree
        def get_total(node):
            if not node:
                return 0
            l = get_total(node.left)
            r = get_total(node.right)
            return l + r + node.val

        # try cutting each edge and compute product
        def test_edges(node):
            if not node:
                return 0

            l = test_edges(node.left)
            r = test_edges(node.right)

            # check product when cutting left or right subtree
            self.res = max(
                self.res,
                l * (total - l),
                r * (total - r)
            )

            return l + r + node.val

        self.res = 0               # store maximum product
        total = get_total(root)    # total sum of tree
        test_edges(root)           # evaluate all cuts

        return self.res % (10**9 + 7)
