class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_len: dict[int, int] = defaultdict(int)

        longest = 0
        for n in nums:
            if num_len[n] != 0:
                continue
            num_len[n] = 1 + num_len[n - 1] + num_len[n + 1]
            num_len[n - num_len[n - 1]] = num_len[n]
            num_len[n + num_len[n + 1]] = num_len[n]
            longest = max(longest, num_len[n])

        return longest