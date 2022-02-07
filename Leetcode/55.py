class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0
        for i, n in enumerate(nums):
            if i > last:
                return False
            last = max(last, i+n)
        return True