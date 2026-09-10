class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        small = 0
        large = len(matrix)

        while small < large:
            mid = (small + large) // 2

            if matrix[mid][0] > target:
                large = mid
            elif matrix[mid][0] <= target:
                small = mid + 1
        
        row = matrix[large - 1]
        left, right = 0, len(row) - 1

        while left < right:
            mid = (left + right) // 2

            if row[mid] >= target:
                right = mid
            elif row[mid] < target:
                left = mid + 1

        return left < len(row) and row[left] == target
