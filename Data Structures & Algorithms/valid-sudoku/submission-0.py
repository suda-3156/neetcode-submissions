class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            if not self.isValid9(row):
                return False

        # column
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])

            if not self.isValid9(col):
                return False

        # sub-box
        for i in range(3):
            for j in range(3):
                nums = []
                for k in range(3):
                    for l in range(3):
                        nums.append(board[3 * i + k][3 * j + l])

                print(i, j, nums)
                if not self.isValid9(nums):
                    return False

        return True

    def isValid9(self, nums: list[str]) -> bool:
        if len(nums) > 9:
            return False

        seen: set[str] = set()

        for n in nums:
            if n == ".":
                continue

            if n in seen:
                return False

            seen.add(n)

        return True
