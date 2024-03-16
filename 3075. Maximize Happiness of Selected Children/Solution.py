class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        h = 0
        for i in range(k):
            n = happiness[i]-i
            if n>0:
                h += n
        return h
