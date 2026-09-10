class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        result = count = 0
        left = right = 0
        seen = set()

        while left <= right and right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
                count += 1

            result = max(result, count)

            while right < len(s) and s[left] != s[right]:
                seen.remove(s[left])
                left += 1
                count -= 1
            
            left += 1
            right += 1

        return result