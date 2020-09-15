# Solution 1: DP.
# Time : O(N), Space: O(1)

# Solution 2: 값들이 Integer이므로 곱하면 절대값은 커져감.
# 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 두번 보면서 누적된 곱의 최대값을 저장해나아가면 됨.
# (-갯수가 홀수일경우에 한쪽 방향으로만 가면 최대값이 아님.)
# n이 0일때는 누적된 곱을 1로 reset 해줌.
# Time : O(N), Space: O(1)


class Solution:
    def maxProduct_2(self, nums: List[int]) -> int:
        ans = float("-inf")
        m = 1
        for n in nums:
            m *= n
            ans = max(ans, m)
            if n == 0:
                m = 1
        m = 1
        for n in reversed(nums):
            m *= n
            ans = max(ans, m)
            if n == 0:
                m = 1
        return ans

    def maxProduct_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret, dp = float("-inf"), [1, 1]
        for n in nums:
            dp = [min(dp[0] * n, dp[1] * n, n), max(dp[0] * n, dp[1] * n, n)]
            ret = max(ret, dp[1])
        return ret
