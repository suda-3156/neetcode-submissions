class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = defaultdict(int)
        freq: list[int] = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for key, val in count.items():
            freq[val].append(key)

        ans: list[int] = []

        for ls in reversed(freq):
            ans += ls
            if len(ans) >= k:
                break

        return ans
