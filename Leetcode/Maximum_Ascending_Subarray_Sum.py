# Time : O(N), Space : O(1)
# 5m

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev, s, ans = 0, 0, float('-inf')
        for n in nums:
            s = s+n if prev < n else n
            prev = n
            ans = max(ans, s)
        return ans
