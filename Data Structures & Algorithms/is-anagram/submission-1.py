class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        times_appeared: list[int] = [0] * 26
        for char in s:
            times_appeared[ord(char) - ord('a')] += 1

        for char in t:
            times_appeared[ord(char) - ord('a')] -= 1

        for num in times_appeared:
            if num != 0:
                return False

        return True
