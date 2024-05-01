class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        newS = ''
        i = 0
        while True:
            newS = word[i] + newS
            if word[i] == ch:
                newS += word[i+1:]
                break
            i += 1
        return newS
