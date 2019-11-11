# Solution 0 : Heuristics. O(N^4), O(1)

# Solution 1 : DP.
# Time : O(MN), Space : O(MN) 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ans = 0
        M, N = len(matrix), len(matrix[0]) 
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for j in range(N):
            for i in range(M):
                if matrix[i][j] == "1":
                    res = 1
                    if i > 0 and j > 0 and dp[i-1][j] > 0 and dp[i][j-1] > 0:
                        res = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
                    dp[i][j] = res
                    ans = max(ans, res*res)
        return ans
