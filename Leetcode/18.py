class Solution:
    def Nsum(self, nums, start, target, n) -> List[List[int]]:
        """
        방법은 그냥 쉽다. Two Pointer를 그냥 반복해서 확장하는 것.
        
        O(N^(n-1)) / O(n)
        """
        N, res = len(nums), []
        if n == 2:
            l, r = start, N-1
            while l < r:
                if target > nums[l]+nums[r]:
                    l += 1
                elif target < nums[l]+nums[r]:
                    r -= 1
                else:
                    res.append([nums[l],nums[r]])
                    # 중복되는 정답 패스하기
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
            return res
        else:
            for i in range(start, N-n+1):
                if i == start or (i > start and nums[i] != nums[i-1]):
                    res.extend([[nums[i]]+l for l in self.Nsum(nums, i+1, target-nums[i], n-1)])
            return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Two pointer를 2개의 index 에 대해 반복.
        """
        nums.sort()
        return self.Nsum(nums, 0, target, 4)