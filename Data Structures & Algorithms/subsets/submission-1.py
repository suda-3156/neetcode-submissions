# 1 -> 1,2 -> 1,2,3
# 2 -> 2,3
# 3

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur: list[int], first: int) -> None:
            res.append(cur.copy())

            for i in range(first, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)
        return res
