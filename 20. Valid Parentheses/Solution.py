class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
            
