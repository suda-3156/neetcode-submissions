class Solution:
    def __init__(self):
        self._zeros = [0] * 26

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        count: list[int] = [0] * 26

        for i in range(n):
            count[ord(s1[i]) - ord("a")] += 1
            count[ord(s2[i]) - ord("a")] -= 1

        print(count)

        if self.isZeros(count):
            return True

        left = 1
        while left <= len(s2) - n:
            count[ord(s2[left - 1]) - ord("a")] += 1
            count[ord(s2[left + n - 1]) - ord("a")] -= 1

            print(left, s2[left: left + n], count)

            if self.isZeros(count):
                return True

            left += 1

        return False

    def isZeros(self, array: list[int]) -> bool:
        return array == self._zeros
