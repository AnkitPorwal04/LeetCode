class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        
        for i in range(len(tickets)):
            if i<=k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k]-1)

        return time
