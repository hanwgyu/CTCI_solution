# Time : O(N), Space : O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, s = float('-inf'), 0
        for num in nums:
            s = s + num if s > 0 else num
            ans = max(ans, s)
        return ans
