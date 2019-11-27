# Solution 1 : 각 원소를 포함하는 increasing subsequence의 최대 갯수를 저장해나아감.
# Time : O(N^2), Space : O(N)
 

class Solution:
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums) 
        dp = [1] * N
        for i in range(1, len(nums)):
            for j in range(0, i): 
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
