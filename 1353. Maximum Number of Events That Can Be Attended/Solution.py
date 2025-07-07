import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        max_day = 0
        for event in events:
            max_day = max(max_day, event[1])
        events.sort()
        #max_day = events[-1][1]

        pq = []
        res = 0
        n = len(events)
        i = 0

        for d in range(1, max_day+1):
            while i<n and events[i][0] <= d:
                heapq.heappush(pq, events[i][1])
                i += 1
            
            while pq and pq[0] < d:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                res += 1
        return res
