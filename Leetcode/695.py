class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            O(MN) / O(MN)
        """
        visited = set()
        M,N = len(grid), len(grid[0])
        
        def dfs(i,j)-> int:
            if 0<= i < M and 0<= j < N and (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    return 1+sum(dfs(i+i_diff, j+j_diff) for i_diff, j_diff in [(1,0), (0,1), (-1,0), (0,-1)])
            return 0
        
        return max(dfs(i,j) for j in range(N) for i in range(M))