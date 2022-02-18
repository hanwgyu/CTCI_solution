class Solution:
    def longestOnes(self, A, K):
        """
        Sliding window 깔끔하게.
        """
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
    
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        """
        Sliding Window..
        
        
        """
        i,j = -1, -1
        zero = 0
        ans = 0
        while j < len(nums):
            if zero <= k:
                j += 1
                if j < len(nums) and nums[j] == 0:
                    zero += 1
            else:
                i += 1
                if nums[i] == 0:
                    zero -= 1
            ans = max(ans, j-i-1)
        return ans
