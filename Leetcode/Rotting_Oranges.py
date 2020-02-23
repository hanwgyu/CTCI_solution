# Time : O(MN), Space : O(MN)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def neighbors(i: int, j: int):
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                    yield ni, nj
            
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                v = grid[i][j]
                if v == 2:
                    q.append((i, j, 0))
        
        res = 0
        while q:
            i, j, t = q.popleft()
            if t > res: res = t
            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, t+1))
        if any(1 in r for r in grid):
            return -1
        return res
