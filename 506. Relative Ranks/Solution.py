class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = score.copy()
        rank.sort(reverse = True)
        ans = []
        for i in score:
            r = rank.index(i)
            if r == 0:
                ans.append("Gold Medal")
            elif r == 1:
                ans.append("Silver Medal")
            elif r == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(r+1))
        return ans
