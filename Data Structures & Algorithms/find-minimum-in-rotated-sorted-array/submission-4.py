class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        # search for the boundary
        while left < right:
            mid = (left + right) // 2

            if nums[0] > nums[mid]:  # the boundary is always on the left side of mid
                right = mid
            else:
                left = mid + 1

        return nums[left]
