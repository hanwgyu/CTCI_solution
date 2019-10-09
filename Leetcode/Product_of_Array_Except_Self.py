# Time : O(N), Space : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for num in nums:
            ans.append(p)
            p *= num
        
        p = 1
        for i in reversed(range(len(nums))):
            ans[i] *= p
            p *= nums[i]
        return ans
