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
        for char in s:
            if char.isalnum():
                result += char

        return result
