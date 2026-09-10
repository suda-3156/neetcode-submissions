from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: dict[str, int] = defaultdict(int)
        left = 0
        n = len(s)
        result = 0

        maxf = 0 # the frequency of the most frequent character in the current window
        for right in range(n):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            while right - left + 1 - maxf > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
