class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        
        return "".join(res)
