from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-w for w in stones]
        
        heapify(min_heap)

        while len(min_heap) > 1:
            x = -heappop(min_heap)
            y = -heappop(min_heap)

            if x == y:
                continue
            if x > y:
                heappush(min_heap, - x + y)

        if len(min_heap) == 1:
            return -min_heap[0]
        else:
            return 0