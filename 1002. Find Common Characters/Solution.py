class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alpha = words[0]
        new_words = []
        for i in words:
            new_words.append(list(i))
        res = []
        for i in alpha:
            c = 0
            for j in new_words:
                if i in j:
                    c += 1
                    j.remove(i)
            if c == len(words):
                res.append(i)
        return res
