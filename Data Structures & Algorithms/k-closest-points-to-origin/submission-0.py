from heapq import nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda l: l[0] ** 2 + l[1] ** 2)
