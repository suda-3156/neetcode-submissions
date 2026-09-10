class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        # included in the rectangle
        left_boundaries: list[int] = [0] * n
        for i in range(n):
            if not stack:
                stack.append(i)
                continue

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1] + 1
            stack.append(i)

        stack = []
        right_boundaries: list[int] = [n - 1] * n
        for i in range(n - 1, -1, -1):
            if not stack:
                stack.append(i)
                continue

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1] - 1
            stack.append(i)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right_boundaries[i] - left_boundaries[i] + 1) * heights[i])

        return max_area
