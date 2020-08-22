# Time : O(N*2^N), Space: O(N*2^N)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            n, a = 0, []
            while i > 0:
                if i % 2 == 1:
                    a.append(nums[n])
                i, n = i >> 1, n + 1
            ans.append(a)
        return ans
