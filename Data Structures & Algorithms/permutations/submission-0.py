class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur: list[int], remainings: list[int]) -> None:
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for i in range(len(remainings)):
                cur.append(remainings[i])
                backtrack(cur, remainings[:i] + remainings[i + 1 :])
                cur.pop()

        backtrack([], nums)
        return res
