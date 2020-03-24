# Solution 1: DP.
# Time : O(N), Space: O(N)

# Solution 2: 값들이 Integer이므로 곱하면 절대값은 커져감. 
# 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 두번 보면서 누적된 곱의 최대값을 저장해나아가면 됨. 
# (-갯수가 홀수일경우에 한쪽 방향으로만 가면 최대값이 아님.)
# n이 0일때는 누적된 곱을 1로 reset 해줌.
# Time : O(N), Space: O(1)

class Solution:
    def maxProduct_2(self, nums: List[int]) -> int:
        ans = float('-inf')
        m = 1
        for n in nums:
            m *= n
            ans = max(ans, m)
            if n == 0: m = 1
        m = 1
        for n in reversed(nums):
            m *= n
            ans = max(ans, m)
            if n == 0: m = 1
        return ans

    def maxProduct_1(self, nums: List[int]) -> int:
        if not nums:
            return None
        ans = nums[0]
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], nums[0]
            
        for i in range(1, len(nums)):
            dp[i][0] = max(max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i]), nums[i])
            dp[i][1] = min(min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i]), nums[i])
            ans = max(ans, dp[i][0])
        return ans
