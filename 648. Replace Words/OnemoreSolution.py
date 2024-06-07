#this solution is specifically for python users and shouldn't be used in an exam or interview!

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            successor = sentence[i]

            for root in dictionary:
                if successor.startswith(root):
                    if len(root) < len(successor):
                        successor = root

            sentence[i] = successor
        return " ".join(sentence)
