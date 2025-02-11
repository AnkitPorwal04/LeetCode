class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            ind = s.find(part)
            if ind == -1:
                break
            s = s[:ind] + s[ind + len(part):]
        return s

