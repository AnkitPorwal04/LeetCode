class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = [3,4,7]
        good = 0
        check = False

        for i in range(1,n+1):
            j = i
        
            while j != 0:
                d = j % 10
                
                if d == 2 or d == 5 or d == 6 or d == 9:
                    check = True
                
                elif d in invalid:
                    check = False
                    break
                
                j = j // 10

            if check:
                good += 1

            check = False        
        
        return good
