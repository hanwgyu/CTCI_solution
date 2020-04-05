# Solution : dfs.
# Time : O(Sum(Permutation(N,k)*k^2)(k=1~N)), Space: O(N)

import copy
class Solution:
    def permute_1(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], n: int) -> List[List[int]]:
            if n == 1:
                return [[nums[0]]]
            ans = []
            for l in dfs(nums, n-1):
                for i in range(n-1):
                    temp = copy.copy(l)
                    temp.insert(i, nums[n-1])
                    ans.append(temp)
                l.append(nums[n-1])
                ans.append(l)
            return ans
        return dfs(nums, len(nums))
