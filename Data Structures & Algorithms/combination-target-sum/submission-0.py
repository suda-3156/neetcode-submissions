class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur: list[int], first: int) -> None:
            if sum(cur) == target:
                res.append(cur[:])
                return
            if sum(cur) > target:
                return

            for i in range(first, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i)
                cur.pop()

        backtrack([], 0)
        return res
