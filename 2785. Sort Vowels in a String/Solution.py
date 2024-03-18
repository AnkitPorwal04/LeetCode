class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        v = []
        for i in s:
            if i in vowels:
                v.append(i)
        v.sort(key=lambda x: ord(x))
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                z = v.pop(0)
                #print(z, i)
                s.pop(i)
                s.insert(i, z)
                #print(s)
        return("".join(s))
