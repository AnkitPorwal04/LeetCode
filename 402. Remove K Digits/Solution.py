class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k>0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        
        #if still left with some k
        stack = stack[:len(stack)-k]

        res = "".join(stack)

        if not res: #if empty string
            return "0"
        else: # to remove heading zeros without converting to int
            i = 0
            while i<len(res) and res[i] == '0':
                i += 1
            return res[i:] if i<len(res) else '0'
