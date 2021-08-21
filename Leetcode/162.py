# binary Search.
# m, m+1를 비교해서 큰 쪽으로 이동하면 한번은 조건을 만족하는 경우가 나오게됨.
# Time : O(logN), Space : O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        l, r, m = 0, N-1, 0
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l
