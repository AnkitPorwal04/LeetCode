class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        # We will input pairs of positive and negative integer with same absolute value
        # so the total sum will become 0
        # loop will go till n//2 as there we will be adding 2 numbers in the array in one iteration
        for i in range(n//2):
            ans.append(i+1)
            ans.append(-(i+1))
        # if the number of integer required is odd then we will add a 0 in the array
        if n%2 != 0:
            ans.append(0)
        return ans
