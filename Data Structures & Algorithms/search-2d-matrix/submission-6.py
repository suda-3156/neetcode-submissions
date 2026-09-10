class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # find a possible row
        left = 0
        right = rows
        while left < right:
            mid = (left + right) // 2

            if matrix[mid][0] >= target:
                right = mid
            else:
                left = mid + 1

        target_row = left
        if target_row >= rows or matrix[target_row][0] > target:
            target_row = left - 1 if left > 0 else 0

        left = 0
        right = cols
        while left < right:
            mid = (left + right) // 2

            if matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid

        print(left, right)
        print(target_row)

        return 0 <= left < cols and matrix[target_row][left] == target

        