class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in s:
        # If any single vowel is found in the string then Alice can win somehow
            if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
                return True
        return False


       # vowels = ['a', 'e', 'i', 'o', 'u']
       # f = False
       # for i in s:
       #     if i in vowels:
       #         f = True
       #         break
       # return True if f else False
