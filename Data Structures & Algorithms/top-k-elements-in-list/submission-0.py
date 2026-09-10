class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = defaultdict(int)

        for n in nums:
            count[n] += 1

        topK = sorted(count.values(), reverse=True)[:k]

        ans: list[int] = []
        for k, v in count.items():
            if v in topK:
                ans.append(k)
                topK.remove(v)

        return ans