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
                additional_area = min(l_max, r_max) - height[left]
                if additional_area > 0:
                    area += additional_area
            elif right > 0:
                right -= 1
                r_max = max(r_max, height[right])
                additional_area = min(l_max, r_max) - height[right]
                if additional_area > 0:
                    area += additional_area
            
        return area