class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())
        l = l[::-1]
        return " ".join(l)
