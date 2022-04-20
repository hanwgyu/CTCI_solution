# Solution : DFS

from collections import defaultdict

class Solution:
    def exist(self, matrix: List[List[str]], word: str) -> bool:
        M, N = len(matrix), len(matrix[0])
        def dfs(i: int, j: int, k: int, visited: Set[Tuple[int, int]]) -> bool:
            if k == len(word): return True
            if i < 0 or i >= M or j < 0 or j >= N or (i,j) in visited or matrix[i][j] != word[k]:
                return False
            visited.add((i,j))
            res = dfs(i, j+1, k+1, visited) or dfs(i, j-1, k+1, visited) or dfs(i+1, j, k+1, visited) or dfs(i-1, j, k+1, visited)
            visited.remove((i,j))
            return res
        return any(dfs(i, j, 0, set()) for i in range(M) for j in range(N))

    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        def dfs(x: int, y: int, index: int, visited: Set[int]) -> bool:
            if (x,y) in visited:
                return False
            visited.add((x,y))
            if board[x][y] == word[index]:
                if index == len(word) - 1:
                    return True
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x_, y_ = x+dx, y+dy
                    if 0 <= x_ < M and 0<= y_ < N:
                        if dfs(x + dx, y + dy, index + 1, visited):
                            return True
            visited.remove((x,y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False

