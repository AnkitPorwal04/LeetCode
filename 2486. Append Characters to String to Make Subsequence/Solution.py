class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spointer = 0
        tpointer = 0

        while tpointer<len(t) and spointer<len(s):
            if t[tpointer] == s[spointer]:
                tpointer+=1
                spointer+=1
            else:
                spointer+=1
        return len(t)-tpointer
