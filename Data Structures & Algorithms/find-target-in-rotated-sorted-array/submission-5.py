class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[0] > nums[mid]:
                right = mid
            else:
                left = mid + 1

        # now the left (== right) indicates the minimum element
        if nums[0] <= target:
            left = 0
        else:
            right = len(nums)
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left if left < len(nums) and nums[left] == target else -1