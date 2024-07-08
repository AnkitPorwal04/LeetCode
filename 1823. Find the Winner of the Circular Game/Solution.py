class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = []
        for i in range(n):
            circle.append(i+1)
        x = k-1
        while len(circle)!=1:
            circle.pop(x)
            x = (x+k-1)%len(circle)
        return(circle[0])
        
