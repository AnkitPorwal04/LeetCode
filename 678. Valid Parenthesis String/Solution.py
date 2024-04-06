class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0
        for i in s:
            if i == '(':
                leftmin, leftmax = leftmin+1, leftmax+1
            elif i == ')':
                leftmin, leftmax = leftmin-1, leftmax-1
            else:
                leftmin, leftmax = leftmin-1, leftmax+1
            if leftmax < 0:
                return False
            if leftmin < 0 : leftmin = 0
        return leftmin==0
            
