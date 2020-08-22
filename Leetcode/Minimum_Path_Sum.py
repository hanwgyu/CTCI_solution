# Solution 1: DP. Time: O(MN), Space: O(MN).

# Solution 2: DP with less memory. Time: O(MN), Space: O(N).


class Solution:
    def minPathSum_2(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        dp = []
        s = 0
        for j in range(num_col):
            s += grid[0][j]
            dp.append(s)
        for i in range(1, num_row):
            pre = dp[0]
            for j in range(num_col):
                dp[j] = min(dp[j], pre) + grid[i][j]
                pre = dp[j]
        return dp[num_col - 1]

    def minPathSum_1(self, grid: List[List[int]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(num_col)] for _ in range(num_row)]
        dp[0][0] = grid[0][0]
        for i in range(num_row):
            for j in range(num_col):
                if j + 1 < num_col:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i][j + 1])
                if i + 1 < num_row:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i + 1][j])
        return dp[num_row - 1][num_col - 1]
