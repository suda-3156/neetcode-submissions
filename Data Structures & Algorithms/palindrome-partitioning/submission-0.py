class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(cur: list[str], first: int) -> None:
            if first == len(s):
                res.append(cur[::])
                return

            for i in range(first, len(s)):
                if self.isPalindrome(s[first : i + 1]):
                    cur.append(s[first : i + 1])
                    backtrack(cur, i + 1)
                    cur.pop()

        backtrack([], 0)
        return res

    def isPalindrome(self, s: str) -> bool:
        return s[::-1] == s
