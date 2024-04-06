class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_Count = 0
        arr = list(s)

        for i in range(len(arr)):
            if arr[i] == '(':
                open_Count += 1
            elif arr[i] == ')':
                if open_Count == 0:
                    arr[i] = '*'
                else:
                    open_Count -= 1

        for i in range(len(arr) - 1, -1, -1):
            if open_Count > 0 and arr[i] == '(':
                arr[i] = '*'
                open_Count -= 1
        
        result = ''.join(c for c in arr if c != '*')

        return result
