class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        l_max = height[0]
        r_max = height[-1]

        while left < right:
            if l_max <= r_max and left < len(height) - 1:
                left += 1
                l_max = max(l_max, height[left])
                # here we can assume that l_max <= r_max so we don't need to take the min
                # and, r_max - height[right] (resp. l_max - height[left]) is always >= 0
                #
                # additional_area = min(l_max, r_max) - height[left]
                # if additional_area > 0:
                #    area += additional_area
                area += l_max - height[left]
            elif right > 0:
                right -= 1
                r_max = max(r_max, height[right])
                area += r_max - height[right]

        return area