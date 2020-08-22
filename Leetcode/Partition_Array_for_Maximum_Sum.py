# Solution : DP. 각 step에서 마지막 원소까지 1~K개의 인접한 원소중 최대 원소의 총합과 이전 dp를 이용함.
# Time : O(NK), Space: O(N)


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)
        dp[1] = A[0]
        for i in range(1, N):
            dp[i + 1], max_val = dp[i] + A[i], A[i]
            for j in range(1, min(i + 1, K)):
                max_val = max(max_val, A[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + max_val * (j + 1))
        return dp[N]
