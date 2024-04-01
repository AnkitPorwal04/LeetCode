class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        for i in range(len(s)-9):
            if s[i:i+10] in s[i+1:]:
                ans.add(s[i:i+10])
        return list(ans)
