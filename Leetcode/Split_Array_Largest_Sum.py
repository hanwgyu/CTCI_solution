# Solution 1 : DP. 
# Time : O(MN^2), Space : O(MN)
# Leetcode 테스트 결과 시간초과

class Solution:
    def splitArray_1(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[float('inf') for _ in range(min(i,m)+1)] for i in range(n+1)]
        
        s = 0
        for i in range(1, n+1):
            s += nums[i-1]
            dp[i][1] = s
        
        for i in range(2,n+1):
            for i_ in range(1,i):
                for j in range(2, min(m, i)+1):
                    dp[i][j] = min(dp[i][j], max(dp[i_][j-1], dp[i][1]-dp[i_][1]) if i_ >= j-1 else float('inf'))
        
        return dp[n][m]
                
