class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap, heapMax = [], 0
        for n in nums:
            tmp = n
            while n%2 == 0:
                n = n // 2
            minHeap.append((n, max(tmp, 2*n)))
            heapMax = max(heapMax, n)
        
        res = float('inf')
        heapq.heapify(minHeap)
        while len(minHeap) == len(nums):
            n, nMax = heapq.heappop(minHeap)
            res = min(res, heapMax - n)

            if n < nMax:
                heapq.heappush(minHeap, (n*2, nMax))
                heapMax = max(heapMax, n*2)
        return res
