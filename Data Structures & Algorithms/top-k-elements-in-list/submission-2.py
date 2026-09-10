class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = defaultdict(int)

        for n in nums:
            count[n] += 1

        heap: list[tuple[int, int]] = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        ans: list[int] = []
        for _, val in heap:
            ans.append(val)

        return ans
