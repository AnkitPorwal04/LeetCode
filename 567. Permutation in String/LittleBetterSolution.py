class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        dic1, dic2 = [0]*26 , [0]*26
        for i in range(len(s1)):
            dic1[ord(s1[i]) - ord('a')] += 1
            dic2[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            matches += (1 if dic1[i] == dic2[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            dic2[index] += 1
            if dic1[index] == dic2[index]:
                matches += 1
            elif dic1[index] + 1 == dic2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            dic2[index] -= 1
            if dic1[index] == dic2[index]:
                matches += 1
            elif dic1[index] - 1 == dic2[index]:
                matches -= 1
            l += 1
        return matches == 26
