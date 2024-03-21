class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap
        min_heap = []
        
        # Iterate through each element in the input array
        for num in nums:
            # Push the current element onto the min-heap
            heapq.heappush(min_heap, num)
            
            # If the size of the min-heap exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Return the root of the min-heap, which will be the kth largest element
        return min_heap[0]
