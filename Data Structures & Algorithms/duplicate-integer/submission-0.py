class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared: dict[int, bool] = {}

        for num in nums:
            if num in appeared:
                return True

            appeared[num] = True

        return False
