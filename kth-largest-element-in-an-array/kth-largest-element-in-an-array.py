from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for i in nums:
            heappush(min_heap, i)
            if len(min_heap) > k:
                heappop(min_heap)
        return heappop(min_heap)
