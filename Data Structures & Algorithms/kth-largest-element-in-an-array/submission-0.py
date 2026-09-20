from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heappush(min_heap, n)
            if len(min_heap) > k:
                heappop(min_heap)

        return min_heap[0]
