import re

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        if ('$' in word) or ('#' in word) or ('@' in word) or (len(word)<3):
            return False
        alpha = 2
        for i in word:
            if i in vowels:
                alpha -= 1
                break
        for i in word:
            if i in consonants:
                alpha -= 1
                break
        if alpha:
            return False
        else:
            return True
