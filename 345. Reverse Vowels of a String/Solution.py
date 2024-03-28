class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_s = []
        for i in s:
            if i in vowels:
                v_s.append(i)
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                #print(s[i])
                #ind = s.index(i)
                s.pop(i)
                s.insert(i, v_s.pop())
                #print(s)
        return("".join(s))
