class Solution:
    def maxDepth(self, s: str) -> int:
        bcount = depth = 0
        for i in s:
            if i == '(':
                bcount += 1
                depth = max(depth, bcount)
            elif i == ')':
                bcount -= 1
        return depth
