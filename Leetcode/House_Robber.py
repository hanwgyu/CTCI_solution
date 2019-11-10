# Solution : DP.
# Time : O(N), Space : O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = [[0,0] for _ in range(N)] # dp[i][0] : i번째 집을 안털었을때, dp[i][1] : i번째 집을 털었을때
        dp[0][1] = nums[0]
        for i, n in enumerate(nums):
            dp[i][0], dp[i][1] = max(dp[i-1][0], dp[i-1][1]), dp[i-1][0] + n
        return max(dp[N-1][0], dp[N-1][1])
