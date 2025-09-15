class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        lis = list(map(str, text.split()))
        for i in lis:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                c += 1
        return c
