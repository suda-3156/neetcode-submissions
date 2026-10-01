class Solution:
    def __init__(self):
        self.letter_map: dict[str, list[str]] = {}

        self.letter_map["2"] = ["a", "b", "c"]
        self.letter_map["3"] = ["d", "e", "f"]
        self.letter_map["4"] = ["g", "h", "i"]
        self.letter_map["5"] = ["j", "k", "l"]
        self.letter_map["6"] = ["m", "n", "o"]
        self.letter_map["7"] = ["p", "q", "r", "s"]
        self.letter_map["8"] = ["t", "u", "v"]
        self.letter_map["9"] = ["w", "x", "y", "z"]

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
