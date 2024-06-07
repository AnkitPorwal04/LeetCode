class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        list_sen = list(sentence.split())

        res = ''
        for i in list_sen:
            min_n = float('inf')
            min_word = ''
            for j in dictionary:
        
                n = len(j)

                if j == i[:n] and n<min_n:
                    min_n = n
                    min_word = j

            if min_n == float('inf'):
                res = res + " " + i
            else:
                res = res + " " + min_word
            
        return res[1:]
