class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        
        # Check each character from 'a' to 'z'
        for char in range(ord('a'), ord('z') + 1):
            char = chr(char)
            min_count = float('inf')  # Start with a very high number
            
            # Find the minimum count of the character in all words
            for word in words:
                count = word.count(char)  # Count the current character in the current word
                min_count = min(min_count, count)  # Keep track of the smallest count
                if min_count == 0:
                    break  # If the character is not in one of the words, we can skip further checking
            
            # Add the character to the result list the required number of times
            result.extend([char] * min_count)
        
        return result
