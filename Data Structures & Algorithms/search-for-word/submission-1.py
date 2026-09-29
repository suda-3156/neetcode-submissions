class Solution:
    def __init__(self) -> None:
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        found = False

        def backtrack(path: list[list[int]]) -> None:
            nonlocal found
            if word[len(path) - 1] != board[path[-1][0]][path[-1][1]]:
                return

            if len(path) == n:
                found = True
                return

            for dy, dx in self.directions:
                ny, nx = path[-1][0] + dy, path[-1][1] + dx

                if not (0 <= ny < len(board)) or not (0 <= nx < len(board[0])):
                    continue

                if [ny, nx] in path:
                    continue

                path.append([ny, nx])
                backtrack(path)
                path.pop()

                if found:
                    break

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack([[i, j]])

                if found:
                    return found

        return found
