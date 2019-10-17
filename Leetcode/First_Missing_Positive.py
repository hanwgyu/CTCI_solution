# Solution : Inplace로 nums를 마치 hash처럼 사용함. 'nums[i]// N'를 라스트 내 i 존재여부 파악에 사용.
# Time : O(N), Space : O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        N = len(nums)
        for i, n in enumerate(nums):
            if n < 0 or n >= N:
                nums[i] = 0
        
        for i, n in enumerate(nums):
            nums[n%N] += N
        
        for i, n in enumerate(nums):
            if n // N == 0:
                return i
        return N
