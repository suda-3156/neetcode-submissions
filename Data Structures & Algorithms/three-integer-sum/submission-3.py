class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans: list[list[int]] = []

        nums.sort() # nlog()
        print(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]

            while left < right:
                cur = nums[left] + nums[right]

                if cur == target:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])        
                    left += 1
                    right -= 1
                elif cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
    
        return ans
