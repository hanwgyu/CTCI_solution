# 문제 설명 : nums는 circular queue. 1을 한 group으로 모으는 최소 스왑 횟수를 구하라.

# 1의 갯수 크기의 window를 sliding 하면서 maximum 1의 갯수를 구함.

# REMIND : sliding window 기본 문제. array를 두배로 늘려서 Sliding Window 를 구하는 테크닉이 중요함.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        N = len(nums)
        res, cur_ones = 0, 0
        for i in range(N * 2):
            if i >= ones and nums[(i-ones)%N] == 1:
                cur_ones -=1
            if nums[i%N] == 1:
                cur_ones += 1
            res = max(res, cur_ones)
        return ones - res    


    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        res, cur_ones = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i-ones] == 1:
                cur_ones -=1
            if nums[i] == 1:
                cur_ones += 1
            res = max(res, cur_ones)
        return ones - res