class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counts = Counter(candidates)
        nums = list(counts.keys())

        def backtrack(cur: list[int], first: int) -> None:
            if sum(cur) == target:
                res.append(cur.copy())
                return

            if sum(cur) > target:
                return

            for i in range(first, len(nums)):
                if counts[nums[i]] <= 0:
                    continue

                counts[nums[i]] -= 1
                cur.append(nums[i])

                backtrack(cur, i)

                counts[nums[i]] += 1
                cur.pop()

        backtrack([], 0)
        return res
