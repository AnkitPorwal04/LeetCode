class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)
            else:
                return(False)
                break
        else:
            return(True)
