from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        if t == s:
            return s

        countT: dict[str, int] = defaultdict(int)
        for c in t:
            countT[c] += 1

        window: dict[str, int] = defaultdict(int)
        matches = 0
        left = 0

        result, resultLen = [-1, -1], float("infinity")

        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in countT and countT[s[right]] == window[s[right]]:
                matches += 1

            while matches == len(countT):
                if right - left + 1 < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    matches -= 1

                left += 1

        left, right = result

        if resultLen == float("infinity"):
            return ""
        else:
            return s[left : right + 1]
