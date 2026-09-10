class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts: list[int] = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for n in counts:
            if n != 0:
                return False

        return True