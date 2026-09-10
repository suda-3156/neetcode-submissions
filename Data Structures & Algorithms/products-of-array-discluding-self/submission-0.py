class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0] * len(nums)

        if nums.count(0) == 1:
            ans = [0] * len(nums)
            zero_idx = nums.index(0)
            nums.remove(0)
            ans[zero_idx] = self.prod(nums)
            return ans

        # nums has no zero
        # use division operator
        prod_all = self.prod(nums)
        ans = []
        for n in nums:
            ans.append(prod_all // n)

        return ans

    def prod(self, nums: list[int]) -> int:
        ans = 1
        for n in nums:
            ans *= n

        return ans
