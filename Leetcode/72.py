# 공통되는 글자와 사이의 글자 수를 최대로 겹치게 만들어야함.
# 변경하는게 제일 횟수가 적게듬.
# 총 변경 횟수 = sum(max(word1 사이글자수,word2 사이글자수))

# DP[i][j]: word1, word2의 첫 i, j 글자까지 처리했을때의 최소 횟수를 저장해나아감
# [POINT] : dp 로직을 설계하는게 핵심. 처음엔 Space O(MN)으로 풀고, 그 이후 공간복잡도를 줄임.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [0 for _ in range(N+1)]
        for j in range(N+1):
            dp[j] = j
        
        for i, c1 in enumerate(word1, start=1):
            dp[0] = i
            dp_last = i-1
            for j, c2 in enumerate(word2, start=1):
                dp_temp = dp[j]
                if c1 == c2:
                    dp[j] = 1 + min(dp[j], dp[j-1], dp_last-1)
                else:
                    dp[j] = 1 + min(dp[j], dp[j-1], dp_last)
                dp_last = dp_temp
        return dp[N]
                    
        
        
        
    def minDistance_1(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M+1):
            dp[i][0] = i
        for j in range(N+1):
            dp[0][j] = j
        
        for i, c1 in enumerate(word1, start=1):
            for j, c2 in enumerate(word2, start=1):
                if c1 == c2:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[M][N]
                    
