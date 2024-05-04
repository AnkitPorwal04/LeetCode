class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        news1 = s1[2]+s1[1]+s1[0]+s1[3]
        if news1 == s2:
            return True
        news2 = news1[0]+news1[3]+news1[2]+news1[1]
        if news2 == s2:
            return True
        news3 = s1[0]+s1[3]+s1[2]+s1[1]
        if news3 == s2:
            return True
        return False 
