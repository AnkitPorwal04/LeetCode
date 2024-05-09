class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uword = word.upper()
        lword = word.lower()
        nword = (word[0].upper())+(word[1:].lower())
        if uword == word or lword == word or nword == word:
            return True
        else:
            return False
