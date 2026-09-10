class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx: dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in num_idx:
                return [num_idx[target - n], i]

            num_idx[n] = i

        return []