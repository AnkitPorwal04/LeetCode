class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_num = 1              # current level number
        max_sum = root.val         # maximum level sum found so far
        level = [root]             # nodes in the current level
        ret = 1                    # level with maximum sum

        while level != []:
            next_level = []        # nodes in the next level
            level_sum = 0          # sum of values in next level
            level_num += 1

            for node in level:
                if node.left:
                    next_level.append(node.left)
                    level_sum += node.left.val

                if node.right:
                    next_level.append(node.right)
                    level_sum += node.right.val

            # update max sum and level if this level is better
            if next_level != [] and level_sum > max_sum:
                max_sum = level_sum
                ret = level_num

            level = next_level     # move to next level

        return ret
