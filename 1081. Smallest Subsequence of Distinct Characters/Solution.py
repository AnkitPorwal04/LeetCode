class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                j = len(stack)-1
                while(j>=0 and stack[j]>s[i] and stack[j] in s[i+1:]):
                    stack.pop()
                    j -= 1
                stack.append(s[i])
        return "".join(stack)
