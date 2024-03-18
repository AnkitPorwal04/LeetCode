class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            iftrue = 1
            for char in word:
                if word.count(char) > chars.count(char):
                    iftrue = 0
            count += len(word) * iftrue
        return count        
                
