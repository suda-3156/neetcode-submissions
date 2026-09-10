class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat nums[i] as an index to the next
        # find the cycle branching point
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
