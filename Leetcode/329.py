# visited + dfs
# REMIND: 모든 주변 노드를 dfs로 방문한 후 visited 결과를 저장.

def memorization(func):
    memory = {}
    def wrapper(*args):
        if args not in memory:
            memory[args] = func(*args)
        return memory[args]
    return wrapper

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        
        @memorization
        def dfs(i,j) -> int:
            ret = 1
            for diff in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i+diff[0], j+diff[1]
                if 0<=x<M and 0<=y<N and matrix[x][y] > matrix[i][j]:
                    ret = max(ret, dfs(x, y)+1)
            return ret
                
        ans = 1
        for j in range(N):
            for i in range(M):
                ans = max(ans, dfs(i, j))
        return ans