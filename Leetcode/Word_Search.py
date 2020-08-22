# Solution : DFS

from collections import defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, index: int, visited) -> bool:
            if visited[(x, y)]:
                return False
            visited[(x, y)] = True
            if board[x][y] == word[index]:
                if index == len(word) - 1:
                    return True
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (
                        x + dx < 0
                        or x + dx >= len(board)
                        or y + dy < 0
                        or y + dy >= len(board[0])
                    ):
                        continue
                    if dfs(x + dx, y + dy, index + 1, visited):
                        return True
            visited[(x, y)] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = defaultdict(bool)
                if dfs(i, j, 0, visited):
                    return True
        return False
