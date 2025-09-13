class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}   # using a set for faster lookup
        dicv = {}
        dicc = {}

        # count frequency of vowels and consonants separately
        for i in s:
            if i in vowels:
                dicv[i] = dicv.get(i, 0) + 1
            else:
                dicc[i] = dicc.get(i, 0) + 1

        # handle cases where string has only vowels or only consonants
        max_vowel = max(dicv.values()) if dicv else 0
        max_consonant = max(dicc.values()) if dicc else 0

        return max_vowel + max_consonant
