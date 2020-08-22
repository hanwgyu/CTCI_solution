# Solution : DFS
# Time : O(MN), Space: O(MN)

from collections import defaultdict


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], visited, i: int, j: int):
            if visited[(i, j)]:
                return
            visited[(i, j)] = True
            for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    i + di < 0
                    or i + di >= len(grid)
                    or j + dj < 0
                    or j + dj >= len(grid[0])
                ):
                    continue
                if grid[i + di][j + dj] == "1":
                    dfs(grid, visited, i + di, j + dj)

        ans = 0
        visited = defaultdict(lambda: False)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[(i, j)] and grid[i][j] == "1":
                    ans += 1
                    dfs(grid, visited, i, j)
        return ans
