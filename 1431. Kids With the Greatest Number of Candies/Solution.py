class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxchodu = max(candies)
        for i in candies:
            if (i + extraCandies) >= maxchodu:
                ans.append(True)
            else:
                ans.append(False)
        return ans
