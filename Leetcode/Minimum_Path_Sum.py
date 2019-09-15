# Solution : DP. Time: O(MN), Space: O(MN).

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(num_col)] for _ in range(num_row)]
        dp[0][0] = grid[0][0]
        for i in range(num_row):
            for j in range(num_col):
                if j+1 < num_col: 
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j] + grid[i][j+1])
                if i+1 < num_row:
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] + grid[i+1][j])
        return dp[num_row-1][num_col-1]
