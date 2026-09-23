class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)
        unique_nums = list(counts.keys())

        def backtrack(cur: list[int], first: int) -> None:
            res.append(cur[:])

            for i in range(first, len(unique_nums)):
                n = unique_nums[i]

                if counts[n] <= 0:
                    continue

                cur.append(n)
                counts[n] -= 1

                backtrack(cur, i)

                cur.pop()
                counts[n] += 1

        backtrack([], 0)
        return res
