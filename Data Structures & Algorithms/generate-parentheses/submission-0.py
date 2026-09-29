class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: list[str], left: int, right: int) -> None:
            if left == right == n:
                res.append("".join(cur))
                return

            if left < n:
                cur.append("(")
                backtrack(cur, left + 1, right)
                cur.pop()

            if left > right:
                cur.append(")")
                backtrack(cur, left, right + 1)
                cur.pop()

            return

        backtrack([], 0, 0)
        return res
