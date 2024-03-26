class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target not in letters:
            letters.append(target)
            letters.sort()
        if target == letters[-1]:
            return letters[0]
        else:
            for i in range(len(letters)):
                if letters[i] == target and letters[i+1] != target:
                    return letters[i+1]
