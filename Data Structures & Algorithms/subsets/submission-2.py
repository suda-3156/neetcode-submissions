# [] -> [1] -> [1, 2] -> [1, 2, 3]
#           -> [1]    -> [1, 3]
#    -> []  -> [2]    -> [2, 3]
#           -> []     -> [3]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur: list[int], first: int) -> None:
            if first >= len(nums):
                res.append(cur[:])
                return

            cur.append(nums[first])
            backtrack(cur, first + 1)
            cur.pop()
            backtrack(cur, first + 1)

        backtrack([], 0)
        return res
