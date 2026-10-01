class Solution:
    def __init__(self):
        self.letter_map: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def backtrack(cur: list[str], idx: int) -> None:
            if len(cur) == len(digits):
                res.append("".join(cur))
                return

            for c in self.letter_map[digits[idx]]:
                cur.append(c)
                backtrack(cur, idx + 1)
                cur.pop()

        if digits == "":
            return res

        backtrack([], 0)
        return res
