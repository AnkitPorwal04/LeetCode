class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = []
        for i in logs:
            if i == '../':
                if folder:
                    folder.pop()
                else: pass
            elif i == './':
                pass
            else:
                folder.append(i)
        return len(folder)
