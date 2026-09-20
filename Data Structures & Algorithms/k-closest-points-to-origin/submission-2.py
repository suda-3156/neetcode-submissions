from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist: dict[int, list[list[int]]] = defaultdict(list)
        min_heap = []

        for x, y in points:
            d = x**2 + y**2
            dist[d].append([x, y])
            heappush(min_heap, d)

        res = []
        for _ in range(k):
            res.append(dist[heappop(min_heap)].pop())
        return res
