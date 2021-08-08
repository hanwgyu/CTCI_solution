# ByteDance 면접 문제

# 고민 1 : 단순히 계산. 이정도는 풀었어야 하는데..
# Time : O(2^(M+N)), Space : O(max(M,N))


# 고민 2 : DP. 이것도 쉽다.. 1번이랑 똑같이 풀면 됨.
# Time : O(MN), Space: O(MN)

# 고민 3 : DP 공간 줄이기
# Time : O(MN), Space: O(M)

class Solution:
    def minDistance_3(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [0 for _ in range(M+1)]
        dp_prev = [0 for _ in range(M+1)]

        for j, c2 in enumerate(word2):
            for i, c1 in enumerate(word1):
                if c1 == c2:
                    dp[i+1] = dp_prev[i] + 1
                else:
                    dp[i+1] = max(dp[i], dp_prev[i+1])
            dp_prev = dp.copy()
        return M + N - 2 * dp[M]

    def minDistance_2(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for j, c2 in enumerate(word2):
            for i, c1 in enumerate(word1):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return M + N - 2 * dp[M][N]

    def minDistance_1(self, word1: str, word2: str) -> int:
        # Longest Common Subsequence
        def lcs(word1: str, m: int, word2: str, n: int) -> int:
            if m == 0 or n == 0:
                return 0
            if word1[m-1] == word2[n-1]:
                return lcs(word1, m-1, word2, n-1) + 1
            else:
                return max(lcs(word1, m, word2, n-1), lcs(word1, m-1, word2, n))

        return len(word1) + len(word2) - 2 * lcs(word1, len(word1), word2, len(word2))
