from collections import defaultdict
from heapq import heapify, heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq: dict[int, int] = defaultdict(int)

        for n in nums:
            num_freq[n] += 1

        freq_num: dict[int, list[int]] = defaultdict(list)
        top_k: list[int] = []

        for val in num_freq.values():
            heappush(top_k, val)

            if len(top_k) > k:
                heappop(top_k)

        top_k = set(top_k)
        ans: list[int] = []

        for key, val in num_freq.items():
            if val in top_k:
                ans.append(key)

        return ans
