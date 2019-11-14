# Solution 0 : Heuristics. O(N^4), O(1)

# Solution 1 : DP.
# Time : O(MN), Space : O(MN) 

# Solution 2 : DP. 공간복잡도 줄임.
# Time : O(MN), Space : O(min(M,N)) 

class Solution:
    def maximalSquare_2(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ans = 0
        M, N = len(matrix), len(matrix[0])
        N_large = True if M > N else False
        S, L = M if N_large else N, N if N_large else M
        current, past = [0] * S, [0] * S
        
        for a in range(L):
            for b in range(S):
                i, j = b if N_large else a, a if N_large else b
                if matrix[i][j] == "1":
                    res = 1
                    if i > 0 and j > 0:
                        res = min(past[b-1] + 1, current[b-1] + 1, past[b] + 1)
                    current[b] = res
                    ans = max(ans, res*res)
            past, current = current, past
            for b in range(S): current[b] = 0
        return ans
    
    
    def maximalSquare_1(self, matrix: List[List[str]]) -> int:
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
