# Time : O(N), Space : O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (int)((len(nums)*(len(nums)+1))/2 - sum(nums))
