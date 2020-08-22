# Time : O(N), Space : O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        ans = 0
        for num in nums:
            if (num + 1) in d:
                l = d[num] + d[num + 1]
                ans = max(ans, l)
        return ans
