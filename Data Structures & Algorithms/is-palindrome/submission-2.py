class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.onlyAlphanum(s.lower())

        left = 0
        right = len(s) - 1

        if len(s) == 1:
            return True

        while left < len(s) and right >= 0 and left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def onlyAlphanum(self, s: str) -> bool:
        result = ""
        alphanum = set(
            [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]
        )

        for char in s:
            if char in alphanum:
                result += char

        return result
