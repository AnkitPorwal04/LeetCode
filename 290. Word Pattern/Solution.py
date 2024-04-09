class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        n = len(s)
        if n != len(pattern):
            return False
        dic = {}
        for i in range(n):
            if pattern[i] in dic.keys():
                if s[i] != dic[pattern[i]]:
                    return False
            elif s[i] in dic.values():
                return False
            dic[pattern[i]] = s[i]
        return True
